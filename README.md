

# Prerequisites for Building

## 0. Clone this repository

Ensure you can access https://github.com/IITK-CGS/platipus-site through a browser.

Clone this repository:

```
git clone https://github.com/IITK-CGS/platipus-site
```

## 1. Install hugo

Download and install the appropriate hugo\_extended version from [here](https://github.com/gohugoio/hugo/releases). As of this writing, I'm using the [hugo_extended_0.121.2_linux-amd64.deb](https://github.com/gohugoio/hugo/releases/download/v0.121.2/hugo_extended_0.121.2_linux-amd64.deb) on Ubuntu 22.04.

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

- The basic editing is to be done in the [content/](./content/) directory, which also has the [\_index.md](./content/_index.md) and [people.md](./content/people.md).

### Updating bibliography

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

The site can be made live for development by `hugo server` while it can be exported to html using the simple command `hugo`. The html files are exported to the [public/](./public/) directory.
