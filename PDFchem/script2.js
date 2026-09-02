		var overlay = document.querySelector(".overlay");
		var linkedImage = document.querySelector("#linked-image");
		var images = document.querySelectorAll("img");
		for (var i = 0; i < images.length; i++) {
			images[i].addEventListener("click", function() {
				linkedImage.src = this.dataset.link;
				overlay.style.display = "block";
			});
		}
		overlay.addEventListener("click", function() {
			overlay.style.display = "none";
		});