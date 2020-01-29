import pytest

BASE_URL = 'http://192.168.1.5:1313'
SITE_PAGES = [
    '/',
    '/pages/about/',
    '/pages/homelab/'
]

POST_NAMES = [
    '25-days-of-c',
    'Ansible-On-Pi-Cluster',
    'ato2019',
    'back-on-arch',
    'back-on-org-mode-for-work',
    'back-to-solus',
    'charmeleon-desktop-design',
    'create-gitlab-runner',
    'creating-a-git-remote',
    'custom-neofetch-ascii-art',
    'dabbling-with-go',
    'docker-quickstart',
    'draft-website-with-jenkins',
    'emacs-update-evil-usepackage',
    'exporting-proxmox-vms',
    'extending-vm-hd',
    'fedora-kde-tb3',
    'getting-an-ipad',
    'how-i-asked-my-groomsmen',
    'issue26',
    'issues-setting-up-ubiquiti-network',
    'large-display-paradox',
    'LFS-Final-Preparation-Steps',
    'LFS-getting-started',
    'LFS-repeated-setup-steps',
    'LFS-SBus-and-binutils',
    'LIA-1-0-beta-released',
    'macos-challenge',
    'my-new-used-x230',
    'my-t470',
    'new-2019-16inch-mbp',
    'new-dotfiles',
    'new-hhkb-pro2',
    'new-lg32qk500w',
    'New-Theme-Immutable',
    'nginx-subdomain-reverse-proxy',
    'org-babel-setup',
    'replace-zfs-mirror-drive',
    'reset-plasma5-monitor-config',
    'scripting-tmux-workspaces',
    'self2019',
    'setting-up-pass',
    'Setting-up-the-pi-cluster',
    'setting-up-tmuxinator',
    'setup-mosh-shell',
    'shell-stuff-find-grep-sub',
    'simple-reverse-ssh-tunnel',
    'snapd-on-arch',
    'sold-my-bonobo',
    'solus-to-fedora',
    'sql-intro',
    'Started-Using-i3blocks',
    'sub-monitor-workflows-with-xrandr',
    'switched-to-joplin-notes',
    'switching-to-bitwarden',
    'switching-to-mesh-network',
    'tmpfs-mount-ramdisk',
    'Trying-out-plasma5',
    'trying-out-seafile',
    'Updating-Pi-Cluster-With-Ansible',
    'upgrading-network-to-ubiquiti',
    'website-switched-to-cryogen',
    'website-switched-to-hugo',
    'website-transition-to-hugo',
    'ZFS-Backups-To-LUKS-External',
]


@pytest.fixture(params=SITE_PAGES)
def page_url(request):
    """Returns the page urls for testing."""
    return BASE_URL + request.param


@pytest.fixture(params=POST_NAMES)
def post_url(request):
    """Returns the post urls for testing."""
    return BASE_URL + '/post/' + request.param.lower()
