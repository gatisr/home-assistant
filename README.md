# Home Assistant

Home Assistant configuration scripts.

## Configuration

* [Configuration](configuration.yaml) - Home Assistant configuration file.

## Shell commands

* [Extract LSM News Date](shell_commands/extract_lsm_zinas_date.py) - Python shell command to extract the date from the [LSM Ziņas vieglajā valodā](https://www.lsm.lv/temas/zinas-vieglaja-valoda/) website.
* [Extract LSM News mp3 URL](shell_commands/extract_lsm_zinas.py) - Python shell command to extract the mp3 URL from the [LSM Ziņas vieglajā valodā](https://www.lsm.lv/temas/zinas-vieglaja-valoda/) website.

## Command line config

_Python packages required: `beautifulsoup4`, `requests`_

* [LSM News](command_line.yaml) - Command line configuration to read shell commands.

## Scripts

* [LSM News](scripts/lsm_news.yaml) - Script to read the latest news from the [LSM](https://www.lsm.lv/) website.
