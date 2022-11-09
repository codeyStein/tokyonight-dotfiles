
config.load_autoconfig(False)


config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

config.set('content.cookies.accept', 'all', 'devtools://*')

config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# Automated Config
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


config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never')
config.bind('tyt', ':open -t https://youtube.com')
config.bind('ts', ':open -t https://start.duckduckgo.com')
config.bind('tg', ':open -t https://github.com')

config.set('completion.height', '25%')

c.fonts.tabs.selected='12px default_family'
# colors
## Tabs
c.colors.tabs.selected.even.bg='#9D7CD8'
c.colors.tabs.selected.odd.bg='#9D7CD8'
c.colors.tabs.bar.bg='#1F2335'
c.colors.tabs.even.bg='#1F2335'
c.colors.tabs.odd.bg='#1A1B26'
## Completion
c.colors.completion.odd.bg='#1F2335'
c.colors.completion.even.bg='#1A1B26'
c.colors.completion.category.bg='#BB9AF7'
c.colors.completion.match.fg='#BB9AF7' 
c.colors.completion.item.selected.bg='#BB9AF7'
c.colors.completion.item.selected.fg='#1F2335'
c.colors.completion.item.selected.match.fg='#fff'
c.colors.completion.scrollbar.bg='#1F2335'
c.colors.completion.scrollbar.fg='#BB9AF7'

