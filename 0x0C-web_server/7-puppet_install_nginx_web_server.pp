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
