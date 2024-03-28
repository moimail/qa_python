from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")

        assert "Гордость и предубеждение и зомби" in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")

        assert collector.get_book_genre("Гордость и предубеждение и зомби") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.set_book_genre("Война и мир", "Драма")

        assert collector.get_books_with_specific_genre("Фантастика") == ["Гордость и предубеждение и зомби"]

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")

        assert collector.get_books_genre() == {"Гордость и предубеждение и зомби": "Фантастика"}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.set_book_genre("Война и мир", "Драма")

        assert collector.get_books_for_children() == ["Гордость и предубеждение и зомби"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.add_book_in_favorites("Гордость и предубеждение и зомби")

        assert collector.get_list_of_favorites_books() == ["Гордость и предубеждение и зомби"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.add_book_in_favorites("Гордость и предубеждение и зомби")
        collector.delete_book_from_favorites("Гордость и предубеждение и зомби")

        assert collector.get_list_of_favorites_books() == []
