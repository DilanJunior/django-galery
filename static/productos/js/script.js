document.addEventListener('DOMContentLoaded', function() {
    // Carrusel de imágenes
    const heroImages = [
        "https://www.google.com/imgres?q=rtx%204080%20t&imgurl=https%3A%2F%2Fasset.msi.com%2Fresize%2Fimage%2Fglobal%2Fproduct%2Fproduct_1668045190e4886ef46b13298d252099c73e055ae6.png62405b38c58fe0f07fcef2367d8a9ba1%2F600.png&imgrefurl=https%3A%2F%2Flatam.msi.com%2FGraphics-Card%2FGeForce-RTX-4080-16GB-GAMING-X-TRIO&docid=V-HJTdcfuYTxNM&tbnid=GY6K-wsz_FBlFM&vet=12ahUKEwjDtIO2x-CLAxVwRDABHRRzKX8QM3oECBcQAA..i&w=600&h=480&hcb=2&ved=2ahUKEwjDtIO2x-CLAxVwRDABHRRzKX8QM3oECBcQAA",
        "https://www.google.com/imgres?q=rtx%204080%20t&imgurl=https%3A%2F%2Fasset.msi.com%2Fresize%2Fimage%2Fglobal%2Fproduct%2Fproduct_1668045190e4886ef46b13298d252099c73e055ae6.png62405b38c58fe0f07fcef2367d8a9ba1%2F600.png&imgrefurl=https%3A%2F%2Flatam.msi.com%2FGraphics-Card%2FGeForce-RTX-4080-16GB-GAMING-X-TRIO&docid=V-HJTdcfuYTxNM&tbnid=GY6K-wsz_FBlFM&vet=12ahUKEwjDtIO2x-CLAxVwRDABHRRzKX8QM3oECBcQAA..i&w=600&h=480&hcb=2&ved=2ahUKEwjDtIO2x-CLAxVwRDABHRRzKX8QM3oECBcQAA",
        "https://www.google.com/imgres?q=rtx%204080%20t&imgurl=https%3A%2F%2Fasset.msi.com%2Fresize%2Fimage%2Fglobal%2Fproduct%2Fproduct_1668045190e4886ef46b13298d252099c73e055ae6.png62405b38c58fe0f07fcef2367d8a9ba1%2F600.png&imgrefurl=https%3A%2F%2Flatam.msi.com%2FGraphics-Card%2FGeForce-RTX-4080-16GB-GAMING-X-TRIO&docid=V-HJTdcfuYTxNM&tbnid=GY6K-wsz_FBlFM&vet=12ahUKEwjDtIO2x-CLAxVwRDABHRRzKX8QM3oECBcQAA..i&w=600&h=480&hcb=2&ved=2ahUKEwjDtIO2x-CLAxVwRDABHRRzKX8QM3oECBcQAA"
    ];
    let currentImageIndex = 0;
    const heroCarousel = document.getElementById('heroCarousel');

    function updateHeroImage() {
        heroCarousel.style.backgroundImage = `url(${heroImages[currentImageIndex]})`;
        heroCarousel.style.backgroundSize = 'cover';
        heroCarousel.style.backgroundPosition = 'center';
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % heroImages.length;
        updateHeroImage();
    }

    updateHeroImage();
    setInterval(nextImage, 5000);

    // Productos
    const products = [
        { id: 1, name: "Abrigo Clásico", price: 299.99, image: "https://sjc.microlink.io/MjsB8cBl3h1vlF95ExIt5i6yjW0a3bmdFqHz0sfwcI45SEonxIFUPyrFLmaWyW9vN02SmlBzMnSs7uKR3_ANTQ.jpeg" },
        { id: 2, name: "Vestido Elegante", price: 199.99, image: "https://sjc.microlink.io/MjsB8cBl3h1vlF95ExIt5i6yjW0a3bmdFqHz0sfwcI45SEonxIFUPyrFLmaWyW9vN02SmlBzMnSs7uKR3_ANTQ.jpeg" },
        // ... (keep your existing products) ...
    ];

    const productGrid = document.querySelector('#productGrid .grid');
    const productsPerPage = 8;
    let currentPage = 1;
    const totalPages = Math.ceil(products.length / productsPerPage);

    // Create pagination numbers
    function createPagination() {
        const paginationContainer = document.createElement('div');
        paginationContainer.className = 'flex justify-center gap-2 mt-8';
        
        // Previous button
        const prevButton = document.createElement('button');
        prevButton.innerHTML = 'Anterior';
        prevButton.className = 'px-4 py-2 bg-wine-700 text-white rounded-md hover:bg-wine-600 disabled:opacity-50';
        prevButton.onclick = () => changePage(currentPage - 1);
        
        // Page numbers
        const pageNumbers = document.createElement('div');
        pageNumbers.className = 'flex gap-2';
        
        // Next button
        const nextButton = document.createElement('button');
        nextButton.innerHTML = 'Siguiente';
        nextButton.className = 'px-4 py-2 bg-wine-700 text-white rounded-md hover:bg-wine-600 disabled:opacity-50';
        nextButton.onclick = () => changePage(currentPage + 1);
        
        paginationContainer.appendChild(prevButton);
        paginationContainer.appendChild(pageNumbers);
        paginationContainer.appendChild(nextButton);
        
        // Replace existing pagination
        const oldPagination = document.querySelector('#productGrid .mt-8');
        oldPagination.replaceWith(paginationContainer);
        
        return { prevButton, pageNumbers, nextButton };
    }

    // Update pagination UI
    function updatePagination(controls) {
        const { prevButton, pageNumbers, nextButton } = controls;
        
        // Update buttons state
        prevButton.disabled = currentPage === 1;
        nextButton.disabled = currentPage === totalPages;
        
        // Update page numbers
        pageNumbers.innerHTML = '';
        for (let i = 1; i <= totalPages; i++) {
            const pageButton = document.createElement('button');
            pageButton.innerHTML = i;
            pageButton.className = `px-4 py-2 rounded-md ${
                currentPage === i 
                    ? 'bg-wine-700 text-white' 
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`;
            pageButton.onclick = () => changePage(i);
            pageNumbers.appendChild(pageButton);
        }
    }

    // Change page function
    function changePage(newPage) {
        if (newPage < 1 || newPage > totalPages) return;
        currentPage = newPage;
        renderProducts();
        updatePagination(paginationControls);
    }

    // Render products with lazy loading
    function renderProducts() {
        const start = (currentPage - 1) * productsPerPage;
        const end = start + productsPerPage;
        const productsToShow = products.slice(start, end);

        /* productGrid.innerHTML = productsToShow.map(product => `
            <div class="group">
                <div class="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-lg bg-gray-200">
                    <img 
                        data-src="${product.image}" 
                        alt="${product.name}" 
                        class="h-full w-full object-cover object-center group-hover:opacity-75 lazy"
                        src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1 1'%3E%3C/svg%3E"
                    >
                </div>
                <h3 class="mt-4 text-sm text-gray-700">${product.name}</h3>
                <p class="mt-1 text-lg font-medium text-gray-900">$${product.price.toFixed(2)}</p>
            </div>
        `).join(''); */

        // Initialize lazy loading for new images
        initLazyLoading();
    }

    // Lazy loading implementation
    function initLazyLoading() {
        const lazyImages = document.querySelectorAll('img.lazy');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        }, {
            root: null,
            rootMargin: '50px',
            threshold: 0.1
        });

        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // Initialize pagination controls
    const paginationControls = createPagination();
    
    // Initial render
    renderProducts();
    updatePagination(paginationControls);
});
