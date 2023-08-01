import datetime

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Public Cloud'
author = 'Canonical Group Ltd'
copyright = "%s, %s" % (datetime.date.today().year, author)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_tabs.tabs',
    'sphinx_reredirects']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.sphinx']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_last_updated_fmt = ""
html_permalinks_icon = "¶"
html_theme_options = {
    "light_css_variables": {
        "color-sidebar-background-border": "none",
        "font-stack": "Ubuntu, -apple-system, Segoe UI, Roboto, Oxygen, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif",
        "font-stack--monospace": "Ubuntu Mono, Consolas, Monaco, Courier, monospace",
        "color-foreground-primary": "#111",
        "color-foreground-secondary": "var(--color-foreground-primary)",
        "color-foreground-muted": "#333",
        "color-background-secondary": "#FFF",
        "color-background-hover": "#f2f2f2",
        "color-brand-primary": "#111",
        "color-brand-content": "#06C",
        "color-api-background": "#cdcdcd",
        "color-inline-code-background": "rgba(0,0,0,.03)",
        "color-sidebar-link-text": "#111",
        "color-sidebar-item-background--current": "#ebebeb",
        "color-sidebar-item-background--hover": "#f2f2f2",
        "toc-font-size": "var(--font-size--small)",
        "color-admonition-title-background--note": "var(--color-background-primary)",
        "color-admonition-title-background--tip": "var(--color-background-primary)",
        "color-admonition-title-background--important": "var(--color-background-primary)",
        "color-admonition-title-background--caution": "var(--color-background-primary)",
        "color-admonition-title--note": "#24598F",
        "color-admonition-title--tip": "#24598F",
        "color-admonition-title--important": "#C7162B",
        "color-admonition-title--caution": "#F99B11",
        "color-highlighted-background": "#EbEbEb",
        "color-link-underline": "var(--color-background-primary)",
        "color-link-underline--hover": "var(--color-background-primary)",
    },
    "dark_css_variables": {
        "color-foreground-secondary": "var(--color-foreground-primary)",
        "color-foreground-muted": "#CDCDCD",
        "color-background-secondary": "var(--color-background-primary)",
        "color-background-hover": "#666",
        "color-brand-primary": "#fff",
        "color-brand-content": "#06C",
        "color-sidebar-link-text": "#f7f7f7",
        "color-sidebar-item-background--current": "#666",
        "color-sidebar-item-background--hover": "#333",
        "color-admonition-background": "transparent",
        "color-admonition-title-background--note": "var(--color-background-primary)",
        "color-admonition-title-background--tip": "var(--color-background-primary)",
        "color-admonition-title-background--important": "var(--color-background-primary)",
        "color-admonition-title-background--caution": "var(--color-background-primary)",
        "color-admonition-title--note": "#24598F",
        "color-admonition-title--tip": "#24598F",
        "color-admonition-title--important": "#C7162B",
        "color-admonition-title--caution": "#F99B11",
        "color-highlighted-background": "#666",
        "color-link-underline": "var(--color-background-primary)",
        "color-link-underline--hover": "var(--color-background-primary)",
    },
}


html_static_path = ['.sphinx/_static']
html_css_files = [
    'custom.css'
]

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: "explanation/old-name.html": "../how-to/prettify.html",
redirects = {
    "aws/index": 
        "https://canonical-aws.readthedocs-hosted.com/en/latest/",
    "aws/ec2/ec2-how-to/find-ubuntu-images": 
        "https://canonical-aws.readthedocs-hosted.com/en/latest/aws-how-to/find-ubuntu-images/",
    "aws/ec2/ec2-how-to/upgrade-from-focal-to-jammy": 
        "https://canonical-aws.readthedocs-hosted.com/en/latest/aws-how-to/upgrade-from-focal-to-jammy/",
    "aws/eks/eks-how-to/deploy-ubuntu-pro-cluster": 
        "https://canonical-aws.readthedocs-hosted.com/en/latest/aws-how-to/deploy-ubuntu-pro-cluster/",
    "aws/eks/eks-reference/image-retention-policy": 
        "https://canonical-aws.readthedocs-hosted.com/en/latest/#eks-image-retention-policy",

    "azure/index": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/",
    "azure/azure-how-to/find-ubuntu-images": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/azure-how-to/find-ubuntu-images/",
    "azure/azure-how-to/get-ubuntu-pro": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/azure-how-to/get-ubuntu-pro/",
    "azure/azure-how-to/install-azure-cli": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/azure-how-to/install-azure-cli/",
    "azure/azure-how-to/upgrade-from-focal-to-jammy": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/azure-how-to/upgrade-from-focal-to-jammy/",
    "azure/azure-reference/azure-security": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/#about-security-on-azure",
    "azure/azure-explanation/faq": 
        "https://canonical-azure.readthedocs-hosted.com/en/latest/#understanding-ubuntu-on-azure",

    "google/index": 
        "https://canonical-gcp.readthedocs-hosted.com/en/latest/",
    "google/gce/gce-how-to/deploy-kubernetes-with-ubuntu-pro": 
        "https://canonical-gcp.readthedocs-hosted.com/en/latest/google-how-to/deploy-kubernetes-with-ubuntu-pro/",
    "google/gce/gce-how-to/upgrade-from-focal-to-jammy": 
        "https://canonical-gcp.readthedocs-hosted.com/en/latest/google-how-to/upgrade-from-focal-to-jammy/",

    "ibm/index": 
        "https://canonical-ibm.readthedocs-hosted.com/en/latest/",
    "ibm/ibm-vpc/ibm-vpc-how-to/upgrade-from-focal-to-jammy": 
        "https://canonical-ibm.readthedocs-hosted.com/en/latest/ibm-how-to/upgrade-from-focal-to-jammy/",

    "oci/index": 
        "https://canonical-oci.readthedocs-hosted.com/en/latest/",
    "oci/oci-how-to/build-ubuntu-pro-container-image":
        "https://canonical-oci.readthedocs-hosted.com/en/latest/#building-ubuntu-pro-oci-images",
    "oci/oci-how-to/create-chiselled-ubuntu-image": 
        "https://canonical-oci.readthedocs-hosted.com/en/latest/oci-how-to/create-chiselled-ubuntu-image/",
    "oci/oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster": 
        "https://canonical-oci.readthedocs-hosted.com/en/latest/oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster/",

    "oracle/index": 
        "https://canonical-oracle.readthedocs-hosted.com/en/latest/",
    "oracle/oracle-how-to/upgrade-from-focal-to-jammy": 
        "https://canonical-oracle.readthedocs-hosted.com/en/latest/oracle-how-to/upgrade-from-focal-to-jammy/"
}
