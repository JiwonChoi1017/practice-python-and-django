from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Choi",
        "date": date(2023, 7, 8),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras consectetur ipsum vitae nibh facilisis egestas. Fusce feugiat turpis vel lorem auctor, a iaculis nisl tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque sit amet sapien facilisis, egestas urna eget, suscipit ligula. Sed gravida viverra dui, id placerat risus pulvinar id. Duis rutrum ac lorem et hendrerit. In auctor at urna eget fermentum. In dapibus ipsum consequat, interdum urna eget, lacinia urna. Vestibulum vitae fringilla enim. Pellentesque eleifend velit id elit mollis, ac vestibulum mauris luctus. Proin rhoncus pellentesque turpis, in vestibulum lorem semper at. Vestibulum pellentesque commodo odio. Cras risus arcu, faucibus quis ullamcorper eu, hendrerit non odio. Duis tempus dapibus ipsum nec cursus. Praesent sagittis iaculis sem, id eleifend dui suscipit id. Pellentesque finibus quam sit amet malesuada finibus.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras consectetur ipsum vitae nibh facilisis egestas. Fusce feugiat turpis vel lorem auctor, a iaculis nisl tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque sit amet sapien facilisis, egestas urna eget, suscipit ligula. Sed gravida viverra dui, id placerat risus pulvinar id. Duis rutrum ac lorem et hendrerit. In auctor at urna eget fermentum. In dapibus ipsum consequat, interdum urna eget, lacinia urna. Vestibulum vitae fringilla enim. Pellentesque eleifend velit id elit mollis, ac vestibulum mauris luctus. Proin rhoncus pellentesque turpis, in vestibulum lorem semper at. Vestibulum pellentesque commodo odio. Cras risus arcu, faucibus quis ullamcorper eu, hendrerit non odio. Duis tempus dapibus ipsum nec cursus. Praesent sagittis iaculis sem, id eleifend dui suscipit id. Pellentesque finibus quam sit amet malesuada finibus.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras consectetur ipsum vitae nibh facilisis egestas. Fusce feugiat turpis vel lorem auctor, a iaculis nisl tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque sit amet sapien facilisis, egestas urna eget, suscipit ligula. Sed gravida viverra dui, id placerat risus pulvinar id. Duis rutrum ac lorem et hendrerit. In auctor at urna eget fermentum. In dapibus ipsum consequat, interdum urna eget, lacinia urna. Vestibulum vitae fringilla enim. Pellentesque eleifend velit id elit mollis, ac vestibulum mauris luctus. Proin rhoncus pellentesque turpis, in vestibulum lorem semper at. Vestibulum pellentesque commodo odio. Cras risus arcu, faucibus quis ullamcorper eu, hendrerit non odio. Duis tempus dapibus ipsum nec cursus. Praesent sagittis iaculis sem, id eleifend dui suscipit id. Pellentesque finibus quam sit amet malesuada finibus.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
]


def get_date(post):
    return post["date"]


# Create your views here.


def starting_page(request):
    # sort(): 元のリスト自体を書き換える破壊的処理。
    # sorted(): 引数にリストを指定するとソートされた新しいリストを返す。元のリストは変更されない非破壊的処理。
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    # next(): 呼び出される度に元のリスト要素を順番に返す。
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
