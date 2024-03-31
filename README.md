PLATIPUS Lab Site
---

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [FAQs - Frequently Asked Questions](#faqs---frequently-asked-questions)
    - [1. How to generate the static site?](#1-how-to-generate-the-static-site)
        - [For deployment](#for-deployment)
        - [For development](#for-development)
    - [2. How to add new members or delete old members?](#2-how-to-add-new-members-or-delete-old-members)
    - [3. How to add new publications?](#3-how-to-add-new-publications)
    - [4. How to customize how the People page is displayed?](#4-how-to-customize-how-the-people-page-is-displayed)
    - [5. How to customize the entries on the Publications page?](#5-how-to-customize-the-entries-on-the-publications-page)
- [Prerequisites for Building](#prerequisites-for-building)
    - [0. Clone this repository](#0-clone-this-repository)
    - [1. Install hugo](#1-install-hugo)
    - [2. Edit content, raw-data, data, static as appropriate](#2-edit-content-raw-data-data-static-as-appropriate)
    - [3. Updating bibliography](#3-updating-bibliography)
    - [4. Export the markdown pages to html](#4-export-the-markdown-pages-to-html)

<!-- markdown-toc end -->

# FAQs - Frequently Asked Questions

- Drop files like images and documents in `./static/` directory.
- Customize CSS in `./assets/css/userstyles.css`.

## 1. How to generate the static site?

### For deployment

Generate static site by running `hugo` with `-b` argument in the project root directory.

```sh
# SITE_BASE_ADDRESS could be http://localhost:8000 or http://localhost:1313 or https://platipus.cgs.iitk.ac.in
hugo -b $SITE_BASE_ADDRESS
```

This will generate pure HTML/CSS/JS pages in `./public/` which can then be copied over to the location where the site is hosted.

### For development

For development, you can simply run `hugo server` in the project root directory.

```sh
hugo server
```

This will start the hugo server and generate the site. It will also live update the site in case you change anything from the files and directories as described below. Restarting the server might be necessary only in rare occasions. If you are building this site for the first time see the section on [Prerequisites for Building](#prerequisites-for-building) below.

## 2. How to add new members or delete old members?

The details about current members and alumni is maintained as .yml files in [./data/current_members/](./data/current_members/) and [./data/past_members.yml](./data/past_members.yml).

Member photos can themselves be placed in [./static/](./static/) directory or an appropriate sub-directory.


## 3. How to add new publications?

Similar to current members and alumni, new publications can be added to [./data/publications/by_year.yml](./data/publications/by_year.yml) and [./data/publications/by_topic.yml](./data/publications/by_topic.yml). However, these qcan be generated automatically from a bibtex file and an accompanying python script.

Therefore, add new publications or modify existing ones in [./raw-data/publications/publications.bib](./raw-data/publications/publications.bib). Then, run the python script [publications_to_yaml.py](./raw-data/publications/publications_to_yaml.py) in the same directory. This script will read the bibtex file and overwrite the `by_year.yml` and `by_topic.yml` files mentioned above. This python script depends on [bib2yaml](https://pypi.org/project/bib2yaml/) which can be installed using pip.

The by_topic sorting takes place through the keywords provided for the entries in the bibtex file.

The pdfs for the publications can themselves be placed in [./static/](./static/) directory or an appropriate sub-directory.

## 4. How to customize how the People page is displayed?

The People page is generated using [./content/people.md](./content/people.md). This uses current\_members.html and past\_members.html shortcodes in [./layouts/shortcodes/](./layouts/shortcodes/).

These shortcodes in turn use the current\_member.html and past\_member.html partials at [./layouts/partials/](./layouts/partials/).

## 5. How to customize the entries on the Publications page?

The Publications pages are generated using the by_year.md and by_topic.md pages in [./content/publications/](./content/publications/) directory. These respectively rely on 

1. The templating code: by-year.html and by-topic.html shortcodes in [./layouts/shortcodes/](./layouts/shortcodes/) in the shortcodes and the partial [./layouts/partials/pub-entry.html](./layouts/partials/pub-entry.html). 
2. The data in [./raw-data/publications/publications.bib](./raw-data/publications/publications.bib). Modifying this is discussed in Q3 above.

# Prerequisites for Building

## 0. Clone this repository

Ensure you can access https://github.com/IITK-CGS/platipus-site through a browser.

Clone this repository:

```
git clone https://github.com/IITK-CGS/platipus-site
```

## 1. Install hugo

Download and install the appropriate hugo\_extended version corresponding to your operating system from [here](https://github.com/gohugoio/hugo/releases). As of this writing, I'm using the [hugo_extended_0.121.2_linux-amd64.deb](https://github.com/gohugoio/hugo/releases/download/v0.121.2/hugo_extended_0.121.2_linux-amd64.deb) on Ubuntu 22.04.

Linux debian files can be installed using `sudo dpkg -i filename.deb`. If there are some missing dependencies, they can be installed using `sudo apt install --fix-broken`.

By the end of this, `hugo` should be installed. You can check the version using:

```
$ hugo version
hugo v0.121.2-6d5b44305eaa9d0a157946492a6f319da38de154+extended linux/amd64 BuildDate=2024-01-05T12:21:15Z VendorInfo=gohugoio
```

Hugo Documentation is available [here](https://gohugo.io/getting-started/) with the template documentation available [here](https://gohugo.io/getting-started/directory-structure/).

## 2. Edit content, raw-data, data, static as appropriate

- The `platipus-site` website is based on the [hugo-theme-notrack](https://github.com/gevhaz/hugo-theme-notrack). This is already available under [themes/notrack/](./themes/notrack/). The `exampleSite` directory has been deleted to save space.

- The hugo configuration for this site lives in [config.toml](./config.toml).

- The basic editing is to be done in the [content/](./content/) directory, which also has the [\_index.md](./content/_index.md) and [people.md](./content/people.md). Information about people itself is in the [data/current_members/](./data/current_members/) and [data/alumni/](./data/alumni/).

## 3. Updating bibliography

1. Bibliography to be updated by the website maintainer lives in [raw-data/publications/publications.bib](./raw-data/publications/publications.bib).
2. After updating the bibtex file, the maintainer is expected to run [publications\_to\_yaml.py](./raw-data/publications/publications_to_yaml.py) file that lives in the same directory. Running this file requires that the python library `bib2yaml` is installed. This can be installed using `pip install bib2yaml`.
3. After `bib2yaml` is installed, run the `publications_to_yaml.py` by changing directory to `raw-data/publications`.

```
cd $PROJECT_ROOT # or open terminal in the project's root/top-level directory
cd raw-data/publications
python publications_to_yaml.py
```

This will update the [by\_year.yml](data/publications/by_year.yml) and [by\_topic.yml](data/publications/by_topic.yml) files in [data/publications/](./data/publications/).

## 4. Export the markdown pages to html

The site can be made live for development by `hugo server` while it can be exported to html using the simple command `hugo`. The html files are exported to the [public/](./public/) directory. The base address for the site can be specified using the `-b` flag, for example `hugo -b https://example.com`. This address should correspond to the location where the site will be deployed.


