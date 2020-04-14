# a class with three resources related to the Network Time Protocol, or NTP
# rules make sure that the NTP package is always upgraded to the latest version
class ntp {
    # write resource types in lowercase when declaring them
    package { 'ntp':
        ensure => latest,
    }
    # contents of the file will be based on the source attribute
    # write resource types in lowercase when declaring them
    file { '/etc/ntp.conf':
        source => 'puppet:///modules/ntp/ntp.conf',
        replace => true,
        # declares relationship
        # configuration file requires the NTP package
        # write resource types in capitalize when referring to them from another resource's attributes
        require => Package['ntp'],
        # notifies the NTP service if the configuration file changes
        # the service will get reloaded with the new settings if changes are made to the contents of the configuration file
        notify => Service['ntp'],
    }
    # enable and run the NTP service
    # write resource types in lowercase when declaring them
    service { 'ntp':
        enable => true,
        ensure => running,
        # service requires the configuration file
        require => File['/etc/ntp.conf'],
    }
}

include ntp

# Run the rules using 'sudo puppet apply -v ntp.pp'
