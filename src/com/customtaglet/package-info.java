/*
 *  File:         package-info.java
 *  
 *  Purpose:      Holds package documentation, for reference purposes.
 *   
 *  Author:       BRAGA, Bruno <bruno.braga@gmail.com>
 * 
 *  Copyright:
 *                Licensed under the Apache License, Version 2.0 (the "License");
 *                you may not use this file except in compliance with the License.
 *                You may obtain a copy of the License at
 * 
 *                http://www.apache.org/licenses/LICENSE-2.0
 * 
 *                Unless required by applicable law or agreed to in writing, software
 *                distributed under the License is distributed on an "AS IS" BASIS,
 *                WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 *                implied. See the License for the specific language governing
 *                permissions and limitations under the License.
 * 
 *  Notes:        This file is part of the project CustomTaglets. More info at:
 *                https://github.com/brunobraga/CustomTaglets
 * 
 *                Bugs, issues and requests are welcome at:
 *                https://github.com/brunobraga/CustomTaglets/issues
 * 
 */
/**
 * This package basically holds custom taglets (or tags) used in javadoc
 * generation that can be useful to avoid repetition or enhance features
 * that may be a burden to the documenting user.
 * 
 * Refer to classes available within this package for additional details
 * on features available here.
 * 
 * <h2>Javadoc Rendering</h2>
 * 
 * Here is a simple example on how to use this package, based on a dummy
 * Android project, where the <i>command-line</i> code can be executed to
 * generate documentation from comments in code:
 * 
 * <p> (example in bash/unix)
 * 
 * <pre>
 * {@code
 * javadoc \
 * -locale en_US \
 * -encoding UTF-8 \
 * -sourcepath src/ \
 * -classpath /usr/local/src/android/platforms/android-7/android.jar \
 * -taglet WikipediaTaglet \
 * -tagletpath docs/libs/taglets/ \
 * -d docs/ \
 * -nohelp \
 * -use \
 * -nodeprecated \
 * -nodeprecatedlist \
 * -version \
 * -verbose \
 * -private \
 * -notree \
 * -overview docs/overview.html \
 * -windowtitle 'AndroidTest Documentation' \
 * -doctitle 'AndroidTest Documentation' \
 * -top '<b>AndroidTest Documentation</b> v1.0' \
 * -header 'com.androidtest v1.0' \
 * -footer 'com.androidtest v1.0' \
 * -bottom '<font size="-1">Created by Bruno Braga &lt;bruno.braga@gmail.com&gt;, at `date +%Y-%m-%d\ %H:%M:%S.%N`.</font>' \
 * -stylesheetfile docs/javadoc.css \
 * -linkoffline http://developer.android.com/reference file:/usr/local/src/android/docs/reference \
 * com.androidtest
 * }
 * </pre>
 * 
 * 
 * @author Bruno Braga &lt;bruno.braga@gmail.com&gt; 
 * 
 * @version 1.0
 */
package com.customtaglet;