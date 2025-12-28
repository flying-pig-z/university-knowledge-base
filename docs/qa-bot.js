(function () {
    const QABot = {
        settings: {
            serverUrl: '',
            knowledgeBaseIds: [],
            botName: 'AI 助手',
            welcomeMessage: '你好！有什么可以帮助你的吗？',
        },
        submitting: false,
        markedLoaded: false,

        /**
         * 初始化 QA Bot
         */
        initialize: function (config) {
            this.settings.serverUrl = config.serverUrl;
            this.settings.knowledgeBaseIds = config.knowledgeBaseIds || [];
            this.settings.botName = config.botName || this.settings.botName;
            this.settings.welcomeMessage = config.welcomeMessage || this.settings.welcomeMessage;

            // 加载 marked.js 库
            this.loadMarked(() => {
                this.render();
            });
        },

        // 动态加载 marked.js
        loadMarked: function (callback) {
            if (window.marked) {
                this.markedLoaded = true;
                callback();
                return;
            }

            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/marked/marked.min.js';
            script.onload = () => {
                this.markedLoaded = true;
                // 配置 marked
                marked.setOptions({
                    breaks: true,        // 支持 GitHub 风格的换行
                    gfm: true,           // 启用 GitHub 风格 Markdown
                    headerIds: false,    // 禁用标题 ID
                    mangle: false,       // 禁用 email 地址混淆
                });
                callback();
            };
            script.onerror = () => {
                console.warn('Failed to load marked.js, falling back to plain text');
                this.markedLoaded = false;
                callback();
            };
            document.head.appendChild(script);
        },

        render: function () {
            // 创建悬浮按钮
            const botIcon = document.createElement('div');
            botIcon.id = 'qa-bot-icon';
            botIcon.innerHTML = QABot.chatIconSvg + '<span>AI 问答</span>';
            document.body.appendChild(botIcon);

            // 创建弹窗容器
            const popupContainer = document.createElement('div');
            popupContainer.id = 'qa-bot-popup-container';
            document.body.appendChild(popupContainer);

            // 创建弹窗
            const botPopup = document.createElement('div');
            botPopup.id = 'qa-bot-popup';
            popupContainer.appendChild(botPopup);

            // 创建消息列表
            const botMessageList = document.createElement('div');
            botMessageList.id = 'qa-bot-message-list';
            botPopup.appendChild(botMessageList);

            // 添加欢迎消息
            const welcomeMessage = document.createElement('div');
            welcomeMessage.classList.add('qa-bot-message');
            welcomeMessage.innerHTML = `
        <div class="qa-bot-message-icon">${QABot.botIconSvg}</div>
        <div class="qa-bot-message-text">${this.settings.welcomeMessage}</div>
      `;
            botMessageList.appendChild(welcomeMessage);

            // 创建输入区域
            const userInput = document.createElement('div');
            userInput.id = 'qa-bot-user-input';
            botPopup.appendChild(userInput);

            // 输入框
            const inputField = document.createElement('input');
            inputField.type = 'text';
            inputField.id = 'qa-bot-question-input';
            inputField.placeholder = '请输入你的问题...';
            userInput.appendChild(inputField);

            // 提交按钮
            const submitButton = document.createElement('button');
            submitButton.id = 'qa-bot-submit-button';
            submitButton.disabled = true;
            submitButton.textContent = '发送';
            userInput.appendChild(submitButton);

            // 加载动画
            const loadingIcon = document.createElement('div');
            loadingIcon.id = 'qa-bot-loading-icon';
            userInput.appendChild(loadingIcon);

            // Powered by 信息
            const poweredBy = document.createElement('div');
            poweredBy.id = 'qa-bot-powered-by';
            poweredBy.innerHTML = `Powered by <a href="#">${this.settings.botName}</a>`;
            botPopup.appendChild(poweredBy);

            // 注册事件监听
            this.bindEvents(botIcon, popupContainer, inputField, submitButton, loadingIcon);
        },

        bindEvents: function (botIcon, popupContainer, inputField, submitButton, loadingIcon) {
            const self = this;

            // 点击图标打开弹窗
            botIcon.addEventListener('click', function () {
                popupContainer.style.display = 'flex';
                inputField.focus();
            });

            // 点击遮罩层关闭弹窗
            popupContainer.addEventListener('click', function (event) {
                if (event.target === popupContainer) {
                    popupContainer.style.display = 'none';
                }
            });

            // ESC 键关闭弹窗
            document.addEventListener('keydown', function (event) {
                if (event.key === 'Escape') {
                    popupContainer.style.display = 'none';
                }
            });

            // Enter 键提交
            inputField.addEventListener('keyup', function (event) {
                if (event.key === 'Enter') {
                    event.preventDefault();
                    submitButton.click();
                }
            });

            // 输入内容时启用/禁用按钮
            inputField.addEventListener('input', function () {
                const question = inputField.value.trim();
                if (!self.submitting) {
                    submitButton.disabled = question === '';
                }
            });

            // 提交问题
            submitButton.addEventListener('click', function () {
                const question = inputField.value.trim();
                if (!question) return;

                self.submitting = true;
                inputField.value = '';
                submitButton.disabled = true;
                submitButton.style.display = 'none';
                loadingIcon.style.display = 'block';

                self.askQuestion(question);
            });
        },

        askQuestion: async function (question) {
            const messageList = document.getElementById('qa-bot-message-list');
            const submitButton = document.getElementById('qa-bot-submit-button');
            const loadingIcon = document.getElementById('qa-bot-loading-icon');

            // 添加用户消息
            const userMessage = document.createElement('div');
            userMessage.classList.add('qa-bot-user-message');
            userMessage.innerHTML = `
        <div class="qa-bot-user-message-icon">${QABot.userIconSvg}</div>
        <div class="qa-bot-user-message-text">${this.escapeHtml(question)}</div>
      `;
            messageList.appendChild(userMessage);
            this.scrollToBottom();

            try {
                // 发送请求到 RAG 接口
                const response = await fetch(this.settings.serverUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        question: question,
                        knowledgeBaseIds: this.settings.knowledgeBaseIds,
                    }),
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const result = await response.json();
                const data = result.data || result;

                // 添加 Bot 回复（使用 Markdown 渲染）
                const botMessage = document.createElement('div');
                botMessage.classList.add('qa-bot-message');
                botMessage.innerHTML = `
          <div class="qa-bot-message-icon">${QABot.botIconSvg}</div>
          <div class="qa-bot-message-text">${this.renderMarkdown(data.answer)}</div>
        `;
                messageList.appendChild(botMessage);

                // 显示相关文档
                if (data.relevantDocuments && data.relevantDocuments.length > 0) {
                    const relatedFiles = document.createElement('div');
                    relatedFiles.classList.add('qa-bot-related-files');

                    let filesHtml = '<div class="qa-bot-related-files-title">📚 参考文档：</div><ul>';
                    data.relevantDocuments.forEach((doc) => {
                        filesHtml += `<li>${this.escapeHtml(doc.noteTitle)}</li>`;
                    });
                    filesHtml += '</ul>';

                    relatedFiles.innerHTML = filesHtml;
                    messageList.appendChild(relatedFiles);
                }

            } catch (error) {
                console.error('QA Bot Error:', error);

                const errorMessage = document.createElement('div');
                errorMessage.classList.add('qa-bot-error-message');
                errorMessage.textContent = '抱歉，请求失败了。请稍后再试。';
                messageList.appendChild(errorMessage);
            } finally {
                this.submitting = false;
                submitButton.disabled = false;
                submitButton.style.display = 'block';
                loadingIcon.style.display = 'none';
                this.scrollToBottom();
            }
        },

        // 使用 marked.js 渲染 Markdown
        renderMarkdown: function (text) {
            if (!text) return '暂无回答';

            if (this.markedLoaded && window.marked) {
                try {
                    return marked.parse(text);
                } catch (e) {
                    console.warn('Markdown parse error:', e);
                    return this.escapeHtml(text).replace(/\n/g, '<br>');
                }
            }

            // fallback: 简单的文本处理
            return this.escapeHtml(text).replace(/\n/g, '<br>');
        },

        escapeHtml: function (text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        },

        scrollToBottom: function () {
            const messageList = document.getElementById('qa-bot-message-list');
            messageList.scrollTop = messageList.scrollHeight;
        },

        // SVG 图标
        botIconSvg: `<svg width="36" height="36" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM12 5C13.66 5 15 6.34 15 8C15 9.66 13.66 11 12 11C10.34 11 9 9.66 9 8C9 6.34 10.34 5 12 5ZM12 19.2C9.5 19.2 7.29 17.92 6 15.98C6.03 13.99 10 12.9 12 12.9C13.99 12.9 17.97 13.99 18 15.98C16.71 17.92 14.5 19.2 12 19.2Z" fill="#4a90d9"/>
    </svg>`,

        userIconSvg: `<svg width="36" height="36" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 12C14.21 12 16 10.21 16 8C16 5.79 14.21 4 12 4C9.79 4 8 5.79 8 8C8 10.21 9.79 12 12 12ZM12 14C9.33 14 4 15.34 4 18V20H20V18C20 15.34 14.67 14 12 14Z" fill="#4a90d9"/>
    </svg>`,

        chatIconSvg: `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2ZM20 16H5.17L4 17.17V4H20V16Z" fill="white"/>
      <path d="M7 9H17V11H7V9ZM7 6H17V8H7V6ZM7 12H14V14H7V12Z" fill="white"/>
    </svg>`,
    };

    window.QABot = QABot;
})();