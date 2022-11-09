# Automated Config
config.load_autoconfig(False)


config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

config.set('content.cookies.accept', 'all', 'devtools://*')

config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

config.set('content.images', True, 'chrome-devtools://*')

config.set('content.images', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome-devtools://*')


# My Config
config.set('content.javascript.enabled', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome://*/*')

config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('window.hide_decoration', True)


## Keybinds
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind('tyt', ':open -t https://youtube.com')
config.bind('ts', ':open -t https://start.duckduckgo.com')
config.bind('tg', ':open -t https://github.com')

## Tabs
c.tabs.padding={"bottom": 5, "left": 10, "right": 10, "top": 5}
c.tabs.favicons.scale=1.5

## Completion
config.set('completion.height', '25%')

c.fonts.tabs.selected='12px default_family'

# colors
purple='#9D7CD8'
cyan='#7DCFFF'
teal='#1ABC9C'
yellow='#E0AF68'
red='#F7778E'
dark='#1F2335'

## Tabs
c.colors.tabs.selected.even.bg=purple
c.colors.tabs.selected.odd.bg=purple
c.colors.tabs.bar.bg=dark
c.colors.tabs.even.bg=dark
c.colors.tabs.odd.bg=dark
## Completion
c.colors.completion.odd.bg=dark
c.colors.completion.even.bg=dark
c.colors.completion.category.bg=purple
c.colors.completion.match.fg=purple
c.colors.completion.item.selected.bg=purple
c.colors.completion.item.selected.fg=dark
c.colors.completion.item.selected.match.fg='white'
c.colors.completion.scrollbar.bg=dark
c.colors.completion.scrollbar.fg=purple
## Statusbar
c.colors.statusbar.normal.bg=dark
c.colors.statusbar.normal.fg=purple
c.colors.statusbar.command.bg=dark
c.colors.statusbar.command.fg=purple
c.colors.statusbar.progress.bg=purple
c.colors.statusbar.url.error.fg=red
c.colors.statusbar.url.fg=purple
c.colors.statusbar.url.hover.fg=cyan
c.colors.statusbar.url.success.http.fg=teal
c.colors.statusbar.url.success.https.fg=teal
c.colors.statusbar.url.warn.fg=yellow

