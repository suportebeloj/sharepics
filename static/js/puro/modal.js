// Get the modal
let modal = document.getElementById("banner-modal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
let imgs = document.querySelectorAll(".open-modal");
let banner_image = document.querySelector('#banner-image-link')
let modalImg = document.getElementById("banner-image-modal");
let captionText = document.getElementById("caption");

banner_image.onclick = function () {
    modal.style.display = "block";
    modalImg.src = this.getAttribute('data-src');
    captionText.innerHTML = this.getAttribute('data-alt');
}

imgs.forEach(item => {
    item.onclick = function () {
        modal.style.display = "block";
        modalImg.src = this.getAttribute('data-src');
        captionText.innerHTML = this.getAttribute('data-alt');
    }
})



/**
 img.onclick = function () {
     modal.style.display = "block";
     modalImg.src = this.getAttribute('data-src');
     captionText.innerHTML = this.getAttribute('data-alt');
 }
 * 
 */

// Get the <span> element that closes the modal
let span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}