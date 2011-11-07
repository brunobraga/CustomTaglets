#!/bin/bash
#
# File:         build.sh
#
# Purpose:      build java class files and generates javadoc documentation
#
# Author:       BRAGA, Bruno <bruno.braga@gmail.com>
#
# Copyright:
#
#               Licensed under the Apache License, Version 2.0 (the "License");
#               you may not use this file except in compliance with the License.
#               You may obtain a copy of the License at
#
#               http://www.apache.org/licenses/LICENSE-2.0
#
#               Unless required by applicable law or agreed to in writing, software
#               distributed under the License is distributed on an "AS IS" BASIS,
#               WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#               implied. See the License for the specific language governing
#               permissions and limitations under the License.
#
# Notes:        This file is part of the project CustomTaglets. More info at:
#               https://github.com/brunobraga/CustomTaglets
#  
#               Bugs, issues and requests are welcome at:
#               https://github.com/brunobraga/CustomTaglets/issues
#

# build the taglets
javac -classpath /usr/lib/jvm/java-6-openjdk/lib/tools.jar src/com/customtaglet/*

# build documentation
javadoc \
-locale en_US \
-encoding UTF-8 \
-sourcepath src/ \
-classpath /usr/lib/jvm/java-6-openjdk/lib/tools.jar \
-d docs/ \
-nohelp \
-use \
-nodeprecated \
-nodeprecatedlist \
-version \
-nonavbar \
-verbose \
-private \
-notree \
-author \
-noindex \
-windowtitle 'CustomTaglets Documentation' \
-doctitle 'CustomTaglets Documentation' \
-top '<b>CustomTaglets Documentation</b> v1.0' \
-header 'CustomTaglets v1.0' \
-footer 'CustomTaglets v1.0' \
-bottom "<font size=\"-1\">Created by Bruno Braga &lt;bruno.braga@gmail.com&gt;, at `date +%Y-%m-%d\ %H:%M:%S.%N`.</font>" \
com.customtaglet

