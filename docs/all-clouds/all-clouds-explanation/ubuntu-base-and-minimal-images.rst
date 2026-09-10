.. meta::
   :description: Learn about Ubuntu base and minimal cloud images, their differences, and about the 'unminimize' command.

.. _ubuntu-base-and-minimal-images:

Ubuntu base and minimal images
==============================

Broadly speaking, Canonical produces two types of images - a base image and a minimal
image. These are available at https://cloud-images.ubuntu.com/ and are available for
all the clouds and for all the Ubuntu releases.


What are base and minimal images?
---------------------------------

Base images are those that are directly derived from Ubuntu Server-like images
and are meant for general consumption.

Minimal images are designed for automated deployment at scale and made available across a range of cloud substrates.
They use the optimised kernels and optimised boot process on their target compute substrate. These images have a
greatly reduced default package set, without many convenience tools for interactive usage. They are much smaller, boot
faster, and will require fewer security updates over time since they have fewer packages installed.

Minimal instances are not intended to be comfortable to use at the command line, but you can apt-get and snap install
anything as usual. The 'unminimize' command will install the standard Ubuntu Server packages if you want to convert a
Minimal instance to a standard Server environment for interactive use.

Since they retain full support for installing from the Ubuntu archive, Minimal Ubuntu images have access to the same
breadth of software, and the same excellent security maintenance, as the base server images. Combined with full Snap
support, anything you can do with base Ubuntu images, you can do with minimal images.

Enterprise support is available for Minimal Ubuntu images in the form of Canonical's Ubuntu Pro on the same terms as
base Ubuntu cloud images.

Where can I find Minimal Ubuntu?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Downloads**

Generic Minimal Ubuntu images for each Ubuntu Release (e.g. 24.04 Noble Numbat) that have not been customized for a
specific cloud are available for direct download as Daily and Release builds at
`<https://cloud-images.ubuntu.com/minimal/>`_.

`Daily builds <https://cloud-images.ubuntu.com/minimal/daily/>`_ are not tested and are made available as-is for
preview.

Once daily builds have been checked for nontrivial package upgrades and have undergone comprehensive testing, they are
published as `Release builds <https://cloud-images.ubuntu.com/minimal/releases/>`_.

**LXD**

Minimal Ubuntu LXD images can be added and launched directly from the cli:

.. code-block:: bash

    lxc remote add --protocol simplestreams ubuntu-minimal https://cloud-images.ubuntu.com/minimal/releases/
    lxc launch ubuntu-minimal:noble


**Public Clouds**

Minimal Ubuntu images which have been customized for a specific cloud are each available for download or launch via
the corresponding cloud service. You can find instructions for how to locate official Ubuntu images elsewhere in this
documentation:

* `Amazon Web Services <https://ubuntu.com/aws/docs/aws-how-to/instances/find-ubuntu-images>`_
* `Google Compute Engine <https://ubuntu.com/gcp/docs/google-how-to/gce/find-ubuntu-images>`_
* `IBM Cloud <https://ubuntu.com/docs/ibm/ibm-how-to/find-ubuntu-images>`_
* `Oracle Cloud Infrastructure <https://ubuntu.com/docs/oracle/oracle-how-to/find-ubuntu-images>`_


State of minimal images from Mantic onwards
-------------------------------------------

From Mantic Minotaur 23.10 onwards (including Noble Numbat 24.04 LTS), we have
worked through the minimal images to make it more efficient and truly minimal
by constructing a `cloud-minimal`_ seed. This seed is the list of basic
packages that we need in a minimal cloud installation. The package list is then
expanded by a program called `germinate`_, which includes the dependencies of
the listed packages in the seed. Combined, we get the `image manifest`_, i.e. the
list of package names and their respective versions you’d expect to see in a
given minimal cloud image.

With this effort, minimal cloud images now are smaller than the Ubuntu 22.04 LTS
minimal images. The package count has dropped from 426 to 288 (difference: 138),
resulting in a much smaller image size. For example, download QCOW2 images have
reduced from 337.19MiB to 226.75MiB (difference: 110.44MiB). This was achieved,
in part, by reducing the packages installed to only those we feel are required
for a functional Ubuntu cloud instance and by removing the installation of
"Recommends" packages. Therefore, the minimal images are faster to boot, deploy,
provision, etc, as compared to the base images.


What is ``unminimize``? What does it do?
----------------------------------------

``unminimize`` is essentially a script that’s shipped in ``/usr/bin`` by a package
called "unminimize". The goal of this ``unminimize`` script is to unminimize the
minimal image and make it as close as possible to a base image. It does this by
re-enabling installation of all documentation in DPKG, restoring system
documentation and man pages, restoring system translations, and then finally
installing some packages on the top, like linux-image-virtual, etc. These
packages make human interaction easier as they include the installation of
basic packages like editors.

To run ``unminimize``, you simply need to call:

``$ sudo unminimize``


.. _cloud-minimal: https://ubuntu-archive-team.ubuntu.com/seeds/ubuntu.noble/cloud-minimal
.. _germinate: https://ubuntu.com/project/docs/staging/release-team/germinate/
.. _image manifest: https://cloud-images.ubuntu.com/minimal/daily/noble/current/noble-minimal-cloudimg-amd64.manifest
