const booksGrid = document.querySelector("#booksGrid");
const searchInput = document.querySelector("#searchInput");
const categoryButtons = document.querySelectorAll(".category-btn");
const emptyState = document.querySelector("#emptyState");
const bookCount = document.querySelector("#bookCount");
const bookCards = Array.from(document.querySelectorAll(".book-card"));

let activeCategory =
  document.querySelector(".category-btn.is-active")?.dataset.category || "Все";

function getBookEnding(count) {
  const lastDigit = count % 10;
  const lastTwoDigits = count % 100;

  if (lastTwoDigits >= 11 && lastTwoDigits <= 14) {
    return "книг";
  }

  if (lastDigit === 1) {
    return "книга";
  }

  if (lastDigit >= 2 && lastDigit <= 4) {
    return "книги";
  }

  return "книг";
}

function updateBooksView() {
  if (!booksGrid) {
    return;
  }

  const query = (searchInput?.value || "").trim().toLowerCase();
  let visibleCount = 0;

  bookCards.forEach((card) => {
    const title = (card.dataset.title || "").toLowerCase();
    const category = card.dataset.category || "";
    const matchesSearch = title.includes(query);
    const matchesCategory = activeCategory === "Все" || category === activeCategory;
    const isVisible = matchesSearch && matchesCategory;

    card.hidden = !isVisible;

    if (isVisible) {
      visibleCount += 1;
    }
  });

  if (bookCount) {
    bookCount.textContent = `${visibleCount} ${getBookEnding(visibleCount)}`;
  }

  if (emptyState) {
    emptyState.hidden = visibleCount > 0;
  }
}

categoryButtons.forEach((button) => {
  button.addEventListener("click", () => {
    activeCategory = button.dataset.category;

    categoryButtons.forEach((item) => item.classList.remove("is-active"));
    button.classList.add("is-active");

    updateBooksView();
  });
});

searchInput?.addEventListener("input", updateBooksView);

updateBooksView();
