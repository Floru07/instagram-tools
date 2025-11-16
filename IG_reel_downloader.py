from instaloader import Instaloader, Post

def download_reel(reel_link) -> None:
    L = Instaloader(
        download_video_thumbnails=False, 
        save_metadata=False, 
        post_metadata_txt_pattern=""
    )
    
    try:
        # "www.instagram.com/reel/SHORTCODE/?lang=en" -> "SHORTCODE"
        shortcode = reel_link.split("/reel/")[1].split("/")[0]

        post = Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=shortcode)
        print(f"Reel downloaded successfully as < {shortcode} >")

    except Exception as e:
        print("Downolad failed:", e)



if __name__ == "__main__":
    reel_link = input("Enter an Instagram reels link: ")
    download_reel(reel_link)
