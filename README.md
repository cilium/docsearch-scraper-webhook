# DocSearch scraper webhook

This repository holds the code of the DocSearch scraper used to power the hosted
version of DocSearch.

If you're looking for a way to add DocSearch to your site, the easiest solution
is to [apply to DocSearch][1]. To run the scraper yourself, you're at the right
place.

## Webhook usage

Deploy the application

Set `APPLICATION_ID` and `API_KEY` environment variables and update `docsearch.config.json` according to your Algolia app

Follow instructions on [using webhooks](https://docs.readthedocs.io/en/stable/guides/build-notifications.html#using-webhook) in the docsearch docs to add `<deployed_webhook_url>/run-docsearch-index` to enable running docsearch scraper on successful builds 


## Installation and Usage

Please check the [dedicated documentation][2] to see how you can install and
run DocSearch yourself.

This project supports Python 3.6+

## Related projects

DocSearch is made of 3 repositories:

- [algolia/DocSearch][3] contains the `docsearch.js` code source and the
  documentation website.
- [algolia/docsearch-configs][4] contains the JSON files representing all the
  configs for all the documentations DocSearch is powering
- [algolia/docsearch-scraper][5] contains the scraper we use to extract data
  from your documentation. The code is open source and you can run it from a
  Docker image

[1]: https://community.algolia.com/docsearch/
[2]: https://community.algolia.com/docsearch/run-your-own.html
[3]: https://github.com/algolia/docsearch
[4]: https://github.com/algolia/docsearch-configs
[5]: https://github.com/algolia/docsearch-scraper
