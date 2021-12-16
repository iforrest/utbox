![Custom badge](https://img.shields.io/endpoint?style=flat-square&url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Finstalls%2F2734)
![Custom badge](https://img.shields.io/endpoint?color=%23&style=flat-square&url=https%3A%2F%2Fsplunkbasebadge.livehybrid.com%2Fv1%2Fdownloads%2F2734)
![contributors-shield](https://img.shields.io/github/contributors/splunk/utbox.svg?style=flat-square)

<div align="center">
<h3 align="center">URL Toolbox</h3>

  <p align="center">
    Building blocks for URL Manipulation in Splunk Enterprise
    <br />
    <br />
    <a href="https://github.com/splunk/utbox/blob/master/utbox/appserver/static/documentation.pdf">Documentation</a>
    ·
    <a href="https://github.com/splunk/utbox/issues">Report Bug</a>
    ·
    <a href="https://splunkbase.splunk.com/app/2734/">Splunkbase</a>
  </p>
</div>

## About The Project

URL Toolbox (UTBox) is a set of building blocks for Splunk specially created for URL manipulation. UTBox has been created to be modular, easy to use and easy to deploy in any Splunk environments. 

One of the core feature of UTBox is to correctly parse URLs and complicated TLDs (Top Level Domain) using the Mozilla Suffix List. Other functions like shannon entropy, counting, suites, meaning ratio, bayesian analysis, etc, are also available.

UTBox has firstly be created for security analysts but may fit other needs as it’s a set of building blocks. UTBox only needs to be deployed on Splunk Search Heads (the bundles will automatically be sent to your Splunk Indexers). Finally, each lookups is shipped with a macro to make it easier to use.

## Getting Started

This section outlines the steps required to use the app on a Splunk Enterprise environment. If you want to develop the code base further, refer to the [Development](##development) section of this README.


### Prerequisites

- **Splunk Enterprise / Cloud**: Refer to [Splunkbase](https://splunkbase.splunk.com/app/2734/) for supported versions.

### Installation

The easiest way to install the URL Toolbox is via the in-product app browser (Manage Apps -> Browse More Apps). It will allow you to install the latest version from [Splunkbase](https://splunkbase.splunk.com/app/2734/).

If you need a specific version of the app or you want to inspect the app bundle before installation, please refer to the [Splunk Documentation](https://docs.splunk.com/Documentation/AddOns/released/Overview/Installingadd-ons) for your respective platform.
This app needs to be installed on the Search tier of your deployment. 

## Usage

This app provides a set of macros that simplify the interaction with the bundled lookups.


### ut_parse_simple

SPL
```
|makeresults count=1 
| eval url="https://splunk.com" 
| `ut_parse_simple(url)`
```

Output
|_time                       |url               |ut_fragment|ut_netloc |ut_params|ut_path|ut_query|ut_scheme|
|----------------------------|------------------|-----------|----------|---------|-------|--------|---------|
|2021-12-16T10:10:14.000+0000|https://splunk.com|None       |splunk.com|None     |None   |None    |https    |

## Development

Coming soon!

## License

Please refer to the [License on Splunkbase.](https://cdn.apps.splunk.com/static/misc/eula.html)

## Acknowledgments

* Cedric Le Roux
* [Ian Forrest](https://github.com/iforrest)