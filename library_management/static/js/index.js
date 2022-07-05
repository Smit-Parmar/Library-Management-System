$(() => {
    const token = window.localStorage.getItem("Authorization");
    console.log({ token });
    if (token) {
        $("#login-signup-link").hide();
        $("#btn-logout").show();
    } else {
        $("#btn-logout").hide();
        $("#login-signup-link").show();
    }

    loadBooks();
});

$("#btn-logout").on('click', logout);

function logout() {
    console.log("Inside Logout!");
    window.localStorage.removeItem("Authorization");
    // window.location.href = "/login-signup";
    window.location.reload();
}

function loadBooks() {
    $.ajax({
        type: "GET",
        url: "/api/v1/book/",
        success: function (result, status, xhr) {
            console.log(result);
            console.log(status);
            console.log(xhr);
            
            for (let index = 0; index < xhr.responseJSON.length; index++) {
                const oBook = xhr.responseJSON[index];
                let sBookDetails = `<article>
                    <div class="single-book-box">
                        <div class="post-thumbnail">
                            <div class="book-list-icon yellow-icon"></div>
                            <a href="books-media-detail-v1.html"><img alt="Book"
                                    src="{% static 'images/books-media/list-view/book-media-01.jpg' %}" /></a>
                        </div>
                        <div class="post-detail">
                            <div class="books-social-sharing">
                                <ul>
                                    <li><a href="#" target="_blank"><i
                                                class="fa fa-facebook"></i></a></li>
                                    <li><a href="#" target="_blank"><i
                                                class="fa fa-twitter"></i></a></li>
                                    <li><a href="#" target="_blank"><i
                                                class="fa fa-google-plus"></i></a></li>
                                    <li><a href="#" target="_blank"><i class="fa fa-rss"></i></a>
                                    </li>
                                    <li><a href="#" target="_blank"><i
                                                class="fa fa-linkedin"></i></a></li>
                                </ul>
                            </div>
                            <div class="optional-links">
                                <ul>
                                    <li>
                                        <a href="#" target="_blank" data-toggle="blog-tags"
                                            data-placement="top" title="Add TO CART">
                                            <i class="fa fa-shopping-cart"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" data-toggle="blog-tags"
                                            data-placement="top" title="Like">
                                            <i class="fa fa-heart"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" data-toggle="blog-tags"
                                            data-placement="top" title="Mail"><i
                                                class="fa fa-envelope"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" data-toggle="blog-tags"
                                            data-placement="top" title="Search">
                                            <i class="fa fa-search"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" data-toggle="blog-tags"
                                            data-placement="top" title="Print">
                                            <i class="fa fa-print"></i>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                            <header class="entry-header">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <h3 class="entry-title">
                                            <a href="books-media-detail-v1.html"> ${oBook.title} </a>
                                        </h3>
                                        <ul>
                                            <li><strong>Author:</strong> ${oBook.author}</li>
                                            <li><strong>ISBN:</strong> 9781581573268</li>
                                        </ul>
                                    </div>
                                    <div class="col-sm-6">
                                        <ul>
                                            <li><strong>Edition:</strong> First editio</li>
                                            <li><strong>Local Availability:</strong> 0 (of 1)</li>
                                            <li>
                                                <div class="rating">
                                                    <strong>Rating: </strong>
                                                    <span>☆</span>
                                                    <span>☆</span>
                                                    <span>☆</span>
                                                    <span>☆</span>
                                                    <span>☆</span>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </header>
                            <div class="entry-content">
                                <p>${oBook.description}</p>
                            </div>
                            <footer class="entry-footer">
                                <a class="btn btn-dark-gray" href="books-media-detail-v1.html">Read
                                    More</a>
                            </footer>
                        </div>
                        <div class="clear"></div>
                    </div>
                </article>`;
                
                $("#book-list").append(sBookDetails);
            }

        },
        error: function (xhr, status, error) {
            console.log(xhr);
            console.log(status);
            console.log(error);
        }
    })
}