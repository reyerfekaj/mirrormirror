if (!('webkitSpeechRecognition' in window)) {
	alert("Sorry, your Browser does not support the Speech API");
} else {
	var recognizing;
	var recognition = new webkitSpeechRecognition();
	recognition.continuous = true;
	recognition.interimResults = true;
	recognition.lang = "en-US";
	reset();
	recognition.onend = reset;

	recognition.onresult = function (e) {
		var textarea = document.getElementById('results');
		for (var i = e.resultIndex; i < e.results.length; ++i) {
			if (e.results[i].isFinal) {
				textarea.value += e.results[i][0].transcript + ' /';			
			}
		}
		var final = "";
		var interim = "";
		for (var i = 0; i < event.results.length; ++i) {
			if (e.results[i].isFinal) {
				final += event.results[i][0].transcript + ' /';
			} else {
				interim += event.results[i][0].transcript;
        }
      }
      final_span.innerHTML = final;
      interim_span.innerHTML = interim;
	}
	
	function reset() {
		recognizing = false;
		button.innerHTML = "Click to Speak";
	}

	function toggleStartStop() {
		if (recognizing) {
			recognition.stop();
			reset();
		} else {
			recognition.start();
			recognizing = true;
			button.innerHTML = "Click to Stop";
			final_span.innerHTML = "";
			interim_span.innerHTML = "";
		}
	}
}