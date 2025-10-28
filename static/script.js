// ---- Moving Tilt Effect ----
const tiltBox = document.getElementById('tilt-box');
const graphicBox = document.querySelector('.graphic-box');

tiltBox.addEventListener('mousemove', (e) => {
  const { width, height, left, top } = tiltBox.getBoundingClientRect();
  const x = e.clientX - left;
  const y = e.clientY - top;
  const rotateX = ((y / height) - 0.5) * 20; // tilt angle
  const rotateY = ((x / width) - 0.5) * 20;

  graphicBox.style.transform = `rotateX(${ -rotateX }deg) rotateY(${ rotateY }deg) scale(1.02)`;
});

tiltBox.addEventListener('mouseleave', () => {
  graphicBox.style.transform = 'rotateX(0deg) rotateY(0deg) rotate(6deg)';
});

// ---- Moving Quotes ----
const quotes = [
  '"Early prediction saves lives."',
  '"AI-driven diagnosis for better health outcomes."',
  '"Detect CKD before symptoms appear."',
  '"Empowering preventive healthcare through AI."'
];

const quoteBox = document.getElementById('quoteBox');
let quoteIndex = 0;

setInterval(() => {
  quoteIndex = (quoteIndex + 1) % quotes.length;
  quoteBox.textContent = quotes[quoteIndex];
}, 5000);


//2nd section
// Wait for the document to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {

    // This will select ALL elements with the class 'card' in your document
    const cards = document.querySelectorAll('.card');

    // Loop through each card and apply event listeners
    cards.forEach(card => {

        // Event for when the mouse moves over the card
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const maxRotate = 8;
            const rotateX = ((y - centerY) / centerY) * -maxRotate;
            const rotateY = ((x - centerX) / centerX) * maxRotate;

            card.style.transition = 'none';

            // Apply the 3D tilt and scale (pop-out)
            card.style.transform = `
                perspective(1000px) 
                scale(1.05) 
                rotateX(${rotateX}deg) 
                rotateY(${rotateY}deg)
            `;
        });

        // Event for when the mouse leaves the card
        card.addEventListener('mouseleave', () => {
            card.style.transition = 'all 0.4s ease';
            card.style.transform = `
                perspective(1000px) 
                scale(1) 
                rotateX(0) 
                rotateY(0)
            `;
        });
    });
});

//3rd section
// Wait for the document to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {

    // This selector will find ALL elements with the class 'card'
    const cards = document.querySelectorAll('.card, .risk-card,.video-card,.cta-box, .social-icon-link'); // Targets both card types

    cards.forEach(card => {

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const maxRotate = 6; // Reduced rotation for a subtle effect
            const rotateX = ((y - centerY) / centerY) * -maxRotate;
            const rotateY = ((x - centerX) / centerX) * maxRotate;

            card.style.transition = 'none'; // Disable transition for smooth mouse tracking
            
            // This JS transform will combine with the CSS hover scale
            card.style.transform = `
                perspective(1000px) 
                scale(1.05) /* Keep the scale from the CSS hover */
                rotateX(${rotateX}deg) 
                rotateY(${rotateY}deg)
            `;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transition = 'all 0.4s ease'; // Re-enable transition for smooth reset
            card.style.transform = `
                perspective(1000px) 
                scale(1) 
                rotateX(0) 
                rotateY(0)
            `;
        });
    });
});

//for assessment form
// document.addEventListener('DOMContentLoaded', () => {

//     // Select all elements you want to have the 3D tilt effect
//     const elements = document.querySelectorAll(
//         '.card, .risk-card, .video-card, .cta-box, .social-icon-link'
//     );

//     // Set the maximum rotation angle
//     const maxRotate = 8; // You can make this number smaller or larger

//     elements.forEach(el => {
//         // --- Mouse Move Event: Tilts the card ---
//         el.addEventListener('mousemove', (e) => {
//             const rect = el.getBoundingClientRect();
            
//             // Get mouse position relative to the element
//             const x = e.clientX - rect.left;
//             const y = e.clientY - rect.top;

//             const centerX = rect.width / 2;
//             const centerY = rect.height / 2;

//             // Calculate rotation
//             const rotateX = ((y - centerY) / centerY) * -maxRotate;
//             const rotateY = ((x - centerX) / centerX) * maxRotate;

//             // Apply the 3D "pop" and tilt
//             // We remove the transition so it tracks the mouse instantly
//             el.style.transition = 'none';
//             el.style.transform = `
//                 perspective(1000px) 
//                 scale(1.05) 
//                 rotateX(${rotateX}deg) 
//                 rotateY(${rotateY}deg)
//             `;
//         });

//         // --- Mouse Leave Event: Resets the card ---
//         el.addEventListener('mouseleave', () => {
//             // Add a transition for a smooth reset
//             el.style.transition = 'all 0.4s ease';
//             // Reset to default state
//             el.style.transform = `
//                 perspective(1000px) 
//                 scale(1) 
//                 rotateX(0) 
//                 rotateY(0)
//             `;
//         });
//     });
// });