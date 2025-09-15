// Multi-language support for WearGB input page
const translations = {
    en: {
        title: "🎮 WearGB",
        subtitle: "Enter ROM URL for your watch",
        label: "Game ROM URL",
        placeholder: "https://example.com/game.gb",
        button: "Send to Watch",
        sendingText: "Sending to Watch...",
        supportedFormats: "Supported formats:",
        supportedSites: "Supported sites:",
        formats: [
            "Game Boy (.gb, .gbc)",
            "Direct download links",
            "ZIP archives (.zip, .7z)"
        ],
        sites: [
            "Google Drive",
            "Dropbox",
            "MediaFire",
            "GitHub Releases",
            "Archive.org",
            "Direct URLs"
        ],
        errors: {
            noSession: "Error: No session ID found in URL",
            sessionUsed: "This session has already been used. Please generate a new QR code.",
            pleaseWait: "Please wait {seconds} seconds before submitting again",
            maxSubmissions: "Maximum submissions reached for this session. Please refresh the page.",
            enterUrl: "Please enter a URL",
            invalidUrl: "Please enter a valid URL",
            urlTooLong: "URL is too long (max 2048 characters)",
            suspiciousUrl: "Invalid URL: Contains suspicious content",
            noRomConfirm: "URL does not seem to contain a Game Boy ROM file (.gb/.gbc). Continue anyway?",
            sending: "Sending URL to your watch..."
        }
    },
    es: {
        title: "🎮 WearGB",
        subtitle: "Ingrese URL del ROM para su reloj",
        label: "URL del ROM del juego",
        placeholder: "https://ejemplo.com/juego.gb",
        button: "Enviar al Reloj",
        sendingText: "Enviando al Reloj...",
        supportedFormats: "Formatos soportados:",
        supportedSites: "Sitios soportados:",
        formats: [
            "Game Boy (.gb, .gbc)",
            "Enlaces de descarga directa",
            "Archivos ZIP (.zip, .7z)"
        ],
        sites: [
            "Google Drive",
            "Dropbox",
            "MediaFire",
            "GitHub Releases",
            "Archive.org",
            "URLs directas"
        ],
        errors: {
            noSession: "Error: No se encontró ID de sesión en la URL",
            sessionUsed: "Esta sesión ya ha sido utilizada. Por favor, genere un nuevo código QR.",
            pleaseWait: "Por favor espere {seconds} segundos antes de enviar de nuevo",
            maxSubmissions: "Máximo de envíos alcanzado para esta sesión. Por favor actualice la página.",
            enterUrl: "Por favor ingrese una URL",
            invalidUrl: "Por favor ingrese una URL válida",
            urlTooLong: "URL demasiado larga (máximo 2048 caracteres)",
            suspiciousUrl: "URL inválida: Contiene contenido sospechoso",
            noRomConfirm: "La URL no parece contener un archivo ROM de Game Boy (.gb/.gbc). ¿Continuar de todos modos?",
            sending: "Enviando URL a su reloj..."
        }
    },
    fr: {
        title: "🎮 WearGB",
        subtitle: "Entrez l'URL de la ROM pour votre montre",
        label: "URL de la ROM du jeu",
        placeholder: "https://exemple.com/jeu.gb",
        button: "Envoyer à la Montre",
        sendingText: "Envoi à la Montre...",
        supportedFormats: "Formats supportés:",
        supportedSites: "Sites supportés:",
        formats: [
            "Game Boy (.gb, .gbc)",
            "Liens de téléchargement direct",
            "Archives ZIP (.zip, .7z)"
        ],
        sites: [
            "Google Drive",
            "Dropbox",
            "MediaFire",
            "GitHub Releases",
            "Archive.org",
            "URLs directes"
        ],
        errors: {
            noSession: "Erreur: Aucun ID de session trouvé dans l'URL",
            sessionUsed: "Cette session a déjà été utilisée. Veuillez générer un nouveau code QR.",
            pleaseWait: "Veuillez attendre {seconds} secondes avant de soumettre à nouveau",
            maxSubmissions: "Maximum de soumissions atteint pour cette session. Veuillez rafraîchir la page.",
            enterUrl: "Veuillez entrer une URL",
            invalidUrl: "Veuillez entrer une URL valide",
            urlTooLong: "URL trop longue (max 2048 caractères)",
            suspiciousUrl: "URL invalide: Contient du contenu suspect",
            noRomConfirm: "L'URL ne semble pas contenir un fichier ROM Game Boy (.gb/.gbc). Continuer quand même?",
            sending: "Envoi de l'URL à votre montre..."
        }
    },
    ja: {
        title: "🎮 WearGB",
        subtitle: "ウォッチ用のROM URLを入力",
        label: "ゲームROM URL",
        placeholder: "https://example.com/game.gb",
        button: "ウォッチに送信",
        sendingText: "ウォッチに送信中...",
        supportedFormats: "対応フォーマット:",
        supportedSites: "対応サイト:",
        formats: [
            "ゲームボーイ (.gb, .gbc)",
            "直接ダウンロードリンク",
            "ZIPアーカイブ (.zip, .7z)"
        ],
        sites: [
            "Google Drive",
            "Dropbox",
            "MediaFire",
            "GitHub Releases",
            "Archive.org",
            "直接URL"
        ],
        errors: {
            noSession: "エラー: URLにセッションIDが見つかりません",
            sessionUsed: "このセッションは既に使用されています。新しいQRコードを生成してください。",
            pleaseWait: "再送信まで{seconds}秒お待ちください",
            maxSubmissions: "このセッションの最大送信回数に達しました。ページを更新してください。",
            enterUrl: "URLを入力してください",
            invalidUrl: "有効なURLを入力してください",
            urlTooLong: "URLが長すぎます（最大2048文字）",
            suspiciousUrl: "無効なURL: 疑わしいコンテンツが含まれています",
            noRomConfirm: "URLにゲームボーイROMファイル（.gb/.gbc）が含まれていないようです。続行しますか？",
            sending: "URLをウォッチに送信中..."
        }
    }
};

// Detect user's language preference
function detectLanguage() {
    // Check URL parameter first
    const urlParams = new URLSearchParams(window.location.search);
    const langParam = urlParams.get('lang');
    if (langParam && translations[langParam]) {
        return langParam;
    }

    // Check localStorage for saved preference
    const savedLang = localStorage.getItem('weargb-language');
    if (savedLang && translations[savedLang]) {
        return savedLang;
    }

    // Detect from browser language
    const browserLang = navigator.language || navigator.userLanguage;
    const shortLang = browserLang.substring(0, 2).toLowerCase();

    // Return language if we have translation, otherwise default to English
    return translations[shortLang] ? shortLang : 'en';
}

// Apply translations to the page
function applyTranslations(lang) {
    const t = translations[lang];

    // Update text content
    document.querySelector('h1').textContent = t.title;
    document.querySelector('.subtitle').textContent = t.subtitle;
    document.querySelector('label[for="urlInput"]').textContent = t.label;
    document.getElementById('urlInput').placeholder = t.placeholder;
    document.getElementById('sendButton').textContent = t.button;

    // Update supported formats
    const formatsColumn = document.querySelector('.examples-column:first-child');
    formatsColumn.querySelector('h3').textContent = t.supportedFormats;
    const formatsList = formatsColumn.querySelector('ul');
    formatsList.innerHTML = t.formats.map(f => `<li>${f}</li>`).join('');

    // Update supported sites
    const sitesColumn = document.querySelector('.examples-column:last-child');
    sitesColumn.querySelector('h3').textContent = t.supportedSites;
    const sitesList = sitesColumn.querySelector('ul');
    sitesList.innerHTML = t.sites.map(s => `<li>${s}</li>`).join('');

    // Update HTML lang attribute
    document.documentElement.lang = lang;

    // Save language preference
    localStorage.setItem('weargb-language', lang);
}

// Get translated error message
function getErrorMessage(key, lang, params = {}) {
    const message = translations[lang].errors[key];
    if (!message) return key;

    // Replace placeholders with params
    return message.replace(/{(\w+)}/g, (match, param) => {
        return params[param] || match;
    });
}

// Export functions for use in main script
window.languageSupport = {
    detectLanguage,
    applyTranslations,
    getErrorMessage,
    translations
};