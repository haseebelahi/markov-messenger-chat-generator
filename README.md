# Markov Messenger Chat Generator
Using Markov Chains to generate new chats from words you and your friends have used in your Messenger conversations. Generate messages which you never actually sent them but will feel like you have :grin:

# Setup Instructions

Follow the following steps to setup and run:

- Install Python
- Install markovify for using Markov Chains `pip install markovify`
- Download your facebook messenger chat info from Settings -> Your Facebook Information -> Download Your Information. Find detailed guidline with screenshots on how to download the messenger chat data from Facebook [here](https://github.com/haseebelahi/markov-messenger-chat-generator/blob/master/README.md#facebook-step-by-step-guide-to-download-messenger-chat-data).
- Extract the downloaded file and copy the `messages/inbox` folder to the root directory.
- Run `python markovify_chat.py t` to train models on the messenger chat with each one of your contacts.
- Run `python markovify_chat.py g [firstname]_[lastname] [firstname]_[lastname] [length of conversation]` e.g `python markovify_chat.py g jane_doe john_doe 5`

# Note

- The chat generator works good when you have a large corpus of data e.g it will work good for contacts with which you have a lot of chat history and won't work well for those who have very little chat history with you.
- _Your Messenger chat data is sensitive and private information, this repository doesn't share or use that info in any way and stays on the machine you are running this project on._

# Facebook Step by Step Guide to Download Messenger Chat Data

- Login into your account on facebook, go to Settings
![](https://i.ibb.co/HTwxf6r/Screen-Shot-2019-03-21-at-12-42-21-AM.png)

- Go to 'Your Facebook Information' tab on the left

![](https://i.ibb.co/w4TvKHP/Screen-Shot-2019-03-21-at-12-53-03-AM.png)

- Go to 'Download Your Information'

![](https://i.ibb.co/CV0NLCp/Screen-Shot-2019-03-21-at-12-56-55-AM.png)

- Select format 'JSON' and 'Media Quality' preferrably low so we can get our data quickly.

![](https://i.ibb.co/MGxc0Qf/Screen-Shot-2019-03-21-at-1-02-09-AM.png)

- Unselect all except 'Messages' and press the **'Create File'** button

![](https://i.ibb.co/w47ntb0/Screen-Shot-2019-03-21-at-1-05-53-AM.png)
