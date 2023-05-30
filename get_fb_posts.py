def get_fb_posts(pages_list, pages_of_posts, posts_per_page, cred, progress_callback=None):

    # import required libraries
    from facebook_scraper import get_posts
    import pandas as pd
    #import datetime

    total_items = len(pages_list)

    # create empty lists to store post info
    usernames = []
    text = []
    time = []
    post_urls = []
    likes = []
    shares = []
    comments = []
    
    # --FETCH POSTS--
    if len(cred[0]) == 0:
        # for every fb page - no credentials provided
        for idx, page in enumerate(pages_list):
            try:
                # for every post
                for post in get_posts(page, pages=pages_of_posts, timeout=90, options={"posts_per_page": posts_per_page, "allow_extra_requests": False}):
                    # filter out posts that are videos and images
                    if (post['video'] == None) & (post['image'] == None):
                        # store post info to lists
                        try:
                            usernames.append(post['username'])
                        except:
                            usernames.append("Unknown")
                        try:
                            text.append(post['text'])
                        except:
                            text.append("Unknown")
                        try:
                            time.append(post['time'])
                        except:
                            time.append("Unknown")
                        try:
                            post_urls.append(post['post_url'])
                        except:
                            post_urls.append("Unknown")
                        try:
                            likes.append(post['likes'])
                        except:
                            likes.append("Unknown")
                        try:
                            shares.append(post['shares'])
                        except:
                            shares.append("Unknown")
                        try:
                            comments.append(post['comments'])
                        except:
                            comments.append("Unknown")
            except:
                continue
            finally:
                # update progress
                if progress_callback:
                    progress = (idx + 1) / total_items * 100
                    progress_callback(progress)
    else:
        # for every fb page - with credentials provided
        for idx, page in enumerate(pages_list):
            try:
                # for every post
                for post in get_posts(page, pages=pages_of_posts, timeout=90, credentials=cred, options={"posts_per_page": posts_per_page, "allow_extra_requests": False}):
                    # filter out posts that are videos and images
                    if (post['video'] == None) & (post['image'] == None):
                        # store post info to lists
                        try:
                            usernames.append(post['username'])
                        except:
                            usernames.append("Unknown")
                        try:
                            text.append(post['text'])
                        except:
                            text.append("Unknown")
                        try:
                            time.append(post['time'])
                        except:
                            time.append("Unknown")
                        try:
                            post_urls.append(post['post_url'])
                        except:
                            post_urls.append("Unknown")
                        try:
                            likes.append(post['likes'])
                        except:
                            likes.append("Unknown")
                        try:
                            shares.append(post['shares'])
                        except:
                            shares.append("Unknown")
                        try:
                            comments.append(post['comments'])
                        except:
                            comments.append("Unknown")
            except:
                continue
            finally:
                # update progress
                if progress_callback:
                    progress = (idx + 1) / total_items * 100
                    progress_callback(progress)
            
    # create a dictionary with keys as column names and values as lists
    data = {
        'Page_Name': usernames,
        'Post_Title': text,
        'Post_Time': time,
        'Post_URL': post_urls,
        'Likes': likes,
        'Shares': shares,
        'Comments': comments
    }

    # create the pandas DataFrame
    df = pd.DataFrame(data)

    # sort the DataFrame by Likes
    sorted_df = df.sort_values(by='Likes', ascending=False)

    # reset index
    sorted_df.reset_index(drop=True, inplace=True)

    return sorted_df