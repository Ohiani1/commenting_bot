import praw

reddit = praw.Reddit(
    client_id="goCW4r2J6JdPhiQDLdS5zg",
    client_secret="JIPIj30b3RuWNBVekK5aXJz-IKKCWg",
    user_agent="reddit bot",
    username="Alternative_Metal_89",
    password="Junior1235",
)

import time
users = set()

def keyword():
  for comment in reddit.subreddit("dropshipping+dropship+Dropshipping_Guide+Dropshipping101+Dropshipsupplier+DropshippingService").streeam.comments():
    try:
      name = comment.author.name
      title = f"Hello, {name}"
      text = "You asked and we answered! As experienced dropshippers, we know selling saturated products can eat into your profits.\n\nTo combat this problem, the Competition Meter team has created a tool that helps you know if a product is untapped, competitive, or saturated! \n\nTo top it all off, we added a feature to the tool that helps users find the cheapest option for any product they want to sell. This will help you minimize your business expenses and increase your profit potential!! \n\nThe tool is a google chrome extension. If you would like to learn more about it, check out our website => https://competitionmeter.com/"

      if name in users:
        continue
      else:
        try:
          users.add(name)
          reddit.redditor(name).message(title, text)
          time.sleep(40)
        except:
            continue
    except:
      time.sleep(300)
      keyword()
      
keyword()
