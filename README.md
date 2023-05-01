[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gbagush/MCServerStatusBot">
    <img src="https://i.ibb.co/3fmB6NJ/logo-minecraft.png" alt="Logo" width="180">
  </a>

<h2 align="center">Minecraft Server Status Discord Bot</h2>

  <p align="center">
    Python script for auto update Minecraft Server Status using Discord Webhook
    <br />
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/gbagush/MCServerStatusBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/gbagush/MCServerStatusBot/issues">Request Feature</a>
  </p>
</div>

<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#demo">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#notes">Notes</a></li>
    <li><a href="#to-do">To Do</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This project is a Python script that updates the status of a Minecraft server using the Discord webhook API. It uses the [discord-webhook](https://github.com/lovvskillz/python-discord-webhook) library and the [mcsrvstat.us](https://mcsrvstat.us/) API to retrieve the server status and send it to a designated Discord webhook.

The script's configuration variables can be easily modified to match the server's information and Discord webhook URL. This project is useful for server admins who want to keep their Discord community informed on the server's availability without the need for manual updates.

Overall, this Python script is a simple and effective way to keep your Discord community up-to-date on your Minecraft server's status.

<!-- DEMO -->
### Demo
![demo](https://i.ibb.co/DVkPwWw/demo.png)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Before using this project, you need to have the following prerequisites:

* Python3 and Python3-pip installed on your machine.
* A Minecraft server running on a publicly accessible host with the `enable-query` option set to `true` in the `server.properties` file.
* A Discord account and access to a Discord server where you have permissions to create and manage webhooks.
* Basic knowledge of Python programming and command line interface.

### Installation

Run on Repl.it:

[![Run on Repl.it](https://repl.it/badge/github/MrMazzone/dotreplit-example)](https://repl.it/github/gbagush/MCServerStatusBot)


1. Clone the repo
   ```sh
   git clone https://github.com/gbagush/MCServerStatusBot.git
   ```
2. Install the required libraries by running
   ```sh
   pip3 install -r requirements.txt
   ```
3. Customize `config.json`

   You can customize the `config.json` file to match your server and Discord webhook settings. Here is an explanation of each field:

   * `WEBHOOK_URL`: The URL of the Discord webhook where the server status will be sent.
   [check how to get Webhook URL](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
   * `MESSAGE_ID`: After the bot sends the first message in a Discord channel, the `MESSAGE_ID` in the `config.json` file will be automatically filled.
   * `SERVER_ADDRESS`: The IP address or domain name of your Minecraft server.
   * `SERVER_PORT`: The port number of your Minecraft server. The default port is 25565.
   * `SERVER_NAME`: A name for your Minecraft server.
   * `FOOTER`: Refers to the additional text displayed at the bottom of a message or document.
   ![FooterExample](https://i.ibb.co/16X7Gqx/footer.png)
   * `SLEEP`: The interval in seconds between each server status update _(default 60 seconds)_

4. Run the script using Python by running the command
   ```sh
   python3 main.py
   ```
<!-- NOTES -->
## Notes
This bot uses the [mcsrvstat.us](https://mcsrvstat.us/) API.

* [mcsrvstat.us](https://mcsrvstat.us/) API is ratelimited to 600 requests per 10 minutes.
* Try not to exceed this limit. If you do, your bots IP address could be blocked for abuse.

<!-- TO DO -->
## To Do
- [ ] Bedrock Server Support
- [ ] Custom embed message

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gbagush/MCServerStatusBot.svg?style=for-the-badge
[contributors-url]: https://github.com/gbagush/MCServerStatusBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gbagush/MCServerStatusBot.svg?style=for-the-badge
[forks-url]: https://github.com/gbagush/MCServerStatusBot/network/members
[stars-shield]: https://img.shields.io/github/stars/gbagush/MCServerStatusBot.svg?style=for-the-badge
[stars-url]: https://github.com/gbagush/MCServerStatusBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/gbagush/MCServerStatusBot.svg?style=for-the-badge
[issues-url]: https://github.com/gbagush/MCServerStatusBot/issues
[license-shield]: https://img.shields.io/github/license/gbagush/MCServerStatusBot.svg?style=for-the-badge
[license-url]: https://github.com/gbagush/MCServerStatusBot/blob/master/LICENSE
