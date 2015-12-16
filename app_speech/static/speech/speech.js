if (!('webkitSpeechRecognition' in window)) {
	alert("Sorry, your Browser does not support the Speech API");
} else {
	var recognizing = false;
	var recognition = new webkitSpeechRecognition();
	recognition.continuous = true;
	recognition.interimResults = true;
	recognition.lang = "en-US";
	recognition.onend = reset;
	var textarea = document.getElementById('speech');
	final_span.innerHTML = textarea.value;
	interim_span.innerHTML = "";

	recognition.onresult = function (e) {
		var interim = "";
		for (var i = e.resultIndex; i < e.results.length; ++i) {
			if (e.results[i].isFinal) {
				textarea.value += e.results[i][0].transcript + ' / ';	
			} else {
				interim += e.results[i][0].transcript;
			}
		}
		final_span.innerHTML = textarea.value;
		interim_span.innerHTML = interim;
	}
	
	function reset() {
		recognizing = false;
		//sb1.innerHTML = "Click to Speak";
		sb1.style.backgroundColor = "transparent";
		start_img.alt = "Start";
	}	

	function toggleStartStop() {
		var data = {'speech_text': textarea.value};
		if (recognizing) {
			recognition.stop();
			reset();
			$.post(URL, data, function(response){
				//console.log(data);
				if(response != 'success'){ alert('Error in getting speech!'); }
			});			
		} else {		
			recognition.start();
			recognizing = true;
			//sb1.innerHTML = "Click to Stop";
			sb1.style.backgroundColor = "green";
			start_img.alt = "Stop";
		}
	}
	
	function postText() {
		var data = {'speech_text': textarea.value};
		$.post(URL, data, function(response){
			//console.log(data)
			if(response != 'success'){ alert('Error in getting speech!'); }
		});			
	}
	
}

