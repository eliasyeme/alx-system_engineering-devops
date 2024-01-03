# This Puppet manifest installs and configures the Nginx web server.
# It ensures that the Nginx package is installed, the Nginx service is running and enabled,
# and sets up the necessary files and configurations for the web server.
# The web server serves a basic "Hello World!" page at the root URL,
# and a custom 404 page at /404.html.
# Additionally, it configures a redirect from /redirect_me to a YouTube video.
# The manifest requires the Nginx package to be installed and notifies the Nginx service to restart
# whenever any of the configuration files are modified.

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html':
  ensure => directory,
  mode   => '0755',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
   listen 80 default_server;
   listen [::]:80 default_server;
   
   root /var/www/html;
   index index.html;
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=cw8tuNZjIf4;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
