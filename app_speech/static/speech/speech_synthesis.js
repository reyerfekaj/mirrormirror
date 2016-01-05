if (!('speechSynthesis' in window)) {
	alert("Sorry, your Browser does not support the Speech API");
} else {
	// Synthesis support. Make your web apps talk!	
	var msg = new SpeechSynthesisUtterance();
	//var voices = window.speechSynthesis.getVoices();
	//msg.voice = voices[10]; // Note: some voices don't support altering params
	msg.voiceURI = 'native';
	msg.volume = 1; // 0 to 1
	msg.rate = 0.8; // 0.1 to 10
	msg.pitch = 1.2; //0 to 2
	msg.text = document.getElementById('transcript').value
	msg.lang = 'en-US';
	//console.log(msg.text);
	
	function toggleStartStop_synthesis() {
		if (!(speechSynthesis.speaking)) {
			speechSynthesis.speak(msg);
			tb1.style.backgroundColor = "green";
			start_img_synthesis.alt = "Stop";
		} else {
			speechSynthesis.cancel();
			tb1.style.backgroundColor = "transparent";
			start_img_synthesis.alt = "Start";
		}
	}
}