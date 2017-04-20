#!/usr/bin/env node

/**
 * Copy Task
 * Copy assets into static folder
 */

const copy = require('copy')
const glob = require('glob')
const clc = require('cli-color')
const del = require('del')

const cwd = process.cwd()
const componentDir = 'frontend/components'
const targetDir = 'dcl/templates/components/'

function start () {
  del([targetDir + '**/*']).then(paths => {
    paths.forEach(path => {
      console.log(clc.green('Deleted: ' + path.replace(cwd, '')))
    })
    findFiles()
  })
}

function findFiles () {
  glob('**/*+(.html|.json)', {
    cwd: componentDir,
    nodir: true
  }, duplicate)
}

function duplicate (error, files) {
  if (!error) {
    copy(files, '../../' + targetDir, {
      cwd: componentDir
    }, report)
  } else {
    throw error
  }
}

function report (error, files) {
  if (!error) {
    files.forEach(file => {
      console.log(clc.green('Copied: ' + file.relative))
    })
  } else {
    throw error
  }
}

start()
