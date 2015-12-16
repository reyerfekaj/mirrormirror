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
		var textarea = document.getElementById('speech');
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
		//sb1.innerHTML = "Click to Speak";
		sb1.style.backgroundColor = "transparent";
		start_img.alt = "Start";
	}

	function toggleStartStop() {
		if (recognizing) {
			recognition.stop();
			// get speech text
			var data = {'speech_text': document.getElementById('speech').value};
			$.post(URL, data, function(response){
				if(response != 'success'){ alert('Error in getting speech!'); }
			});			
			reset();
		} else {
			recognition.start();
			recognizing = true;
			//sb1.innerHTML = "Click to Stop";
			sb1.style.backgroundColor = "green";
			start_img.alt = "Stop";
			final_span.innerHTML = "";
			interim_span.innerHTML = "";
		}
	}
	
	
}

