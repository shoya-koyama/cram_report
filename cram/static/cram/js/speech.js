const text        = document.querySelector('#text');
const voiceSelect = document.querySelector('#voice-select');
const speakBtn    = document.querySelector('#speak-btn');

function appendVoices() {
    const voices = speechSynthesis.getVoices();
    voiceSelect.innerHTML = '';
    voices.forEach(voice => {
      if(!voice.lang.match('ja|en-US')) return;
      const option = document.createElement('option');
      option.value = voice.name;
      option.text  = `${voice.name} (${voice.lang})`;
      option.setAttribute('selected', voice.default);
      voiceSelect.appendChild(option);
    });
}

appendVoices();

speechSynthesis.onvoiceschanged = e => {
    appendVoices();
}

function translateJapaneseToEnglish(japaneseText) {
    const translations = {
      "こんにちは": "Hello",
      "はい": "Yes",
      "いいえ": "No"
      // 他の翻訳をここに追加
    };
    return translations[japaneseText] || japaneseText;
}

speakBtn.addEventListener('click', function() {
    let inputValue = text.value;

    if (/[\u3040-\u30FF]/.test(inputValue)) {
        inputValue = translateJapaneseToEnglish(inputValue);
    }

    const uttr = new SpeechSynthesisUtterance(inputValue);
    uttr.voice = speechSynthesis
      .getVoices()
      .filter(voice => voice.name === voiceSelect.value)[0];
    speechSynthesis.speak(uttr);
});
