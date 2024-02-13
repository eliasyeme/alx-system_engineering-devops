# fix server error by replacing phpp with php


exec {'replace-line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/bin:/usr/sbin:/bin',
}
