source 'https://rubygems.org'

# if any new gem, say github-pages, is added to the file, run
#`bundle update github-pages`

# Stay update with latest github-pages gem
# Reference: https://byparker.com/blog/2014/stay-up-to-date-with-the-latest-github-pages-gem/
#
#require 'json'
#require 'open-uri'
#versions = JSON.parse(open('https://pages.github.com/versions.json').read)

#gem 'github-pages', versions['github-pages']

# Or update github-pages manually by referring to the latest version being used at GitHub
# Reference: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site

gem "github-pages", "~> 228"

# add plugins here
group :jekyll_plugins do
  gem 'jekyll-sitemap'
  gem 'jekyll-feed'
  gem 'jekyll-seo-tag'
end

# Add webrick gem as it is not present in ruby 3
# Reference: https://github.com/github/pages-gem/issues/752

gem 'webrick'
