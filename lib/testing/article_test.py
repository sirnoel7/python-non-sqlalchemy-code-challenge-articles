import pytest
from classes.many_to_many import Article, Magazine, Author


class TestArticle:
    def test_has_title(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_immutable_str(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            article_1.title = 500

        assert isinstance(article_1.title, str)

    def test_title_is_valid(self):
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")

        with pytest.raises(ValueError):
            Article(author, magazine, "Test")

        with pytest.raises(ValueError):
            Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")

    def test_has_an_author(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert article_1.author == author_1
        assert article_2.author == author_2

    def test_author_of_type_author_and_mutable(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            article_1.author = author_2

    def test_has_a_magazine(self):
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert article_1.magazine == magazine_1
        assert article_2.magazine == magazine_2

    def test_magazine_of_type_magazine_and_mutable(self):
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")

        with pytest.raises(AttributeError):
            article_1.magazine = magazine_2

    def test_get_all_articles(self):
        Article.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")

        assert len(Article.all) == 1
        assert article_1 in Article.all
