#!/bin/bash

Pidfile="/var/run/jenkins-slave.pid"

case "$1" in
   start)
      java -jar /home/jenkins/slave_agent/agent.jar -jnlpUrl *** -secret *** -workDir "/home/jenkins" -noCertificateCheck &
      Pid=$!
      if [ -z $Pid ]; then
         printf "%s\n" "Fail"
      else
         echo $Pid > $Pidfile
         printf "%s\n" "Ok"
      fi
      ;;

   stop)
      printf "%-50s" "Stopping $Name"
      Pid=`cat $Pidfile`
      if [ -f $Pidfile ]; then
         kill -TERM $Pid
         printf "%s\n" "Ok"
         rm -f $Pidfile
      else
         printf "%s\n" "pidfile not found"
      fi
      ;;

   restart)
      $0 stop
      $0 start
      ;;

   status)
      printf "%-50s" "Checking $Name..."
      if [ -f $Pidfile ]; then
         Pid=`cat $Pidfile`
         if [ -z "`ps axf | grep ${Pid} | grep -v grep`" ]; then
            printf "%s\n" "Process dead but pidfile exists"
            echo "Pidfile: $Pidfile"
         else
            echo "Running"
            echo "Pid: $Pid"
            echo "Pidfile: $Pidfile"
         fi
      else
         printf "%s\n" "Service not running"
      fi
      ;;

   *)
      echo "Usage: $0 {start|stop|restart}"
      ;;
esac
