// Get the modal
let modal = document.getElementById("banner-modal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
let img = document.getElementById("banner-image-link");
let modalImg = document.getElementById("banner-image-modal");
let captionText = document.getElementById("caption");
img.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.getAttribute('data-src');
    console.log(modalImg)
    captionText.innerHTML = this.getAttribute('data-alt');
}

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}