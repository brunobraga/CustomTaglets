/*
 *  File:	      WikipediaTaglet.java
 *  
 *  Purpose:      Custom taglet used by javadoc in documentation generation
 *                to facilitate use of Wikipedia links. See this class 
 *                documentation for details.
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
package com.customtaglet;

import com.sun.tools.doclets.Taglet;
import com.sun.javadoc.*;
import java.util.Map;

/**
 * A Taglet representing <i>{&#064;wikipedia target[ title]}</i>. 
 * This tag can be used in any kind of {@link com.sun.javadoc.Doc}.  
 * It is an inline tag, so it relies on extended information
 * within the brackets to build the link to Wikipedia website.  
 * <h2>Examples</h2>
 * "{&#064;wikipedia test}" would be shown as:
 * <a href="http://en.wikipedia.org/test">test</a>
 * <p>
 * "{&#064;wikipedia test My Test}" would be shown as:
 * <a href="http://en.wikipedia.org/test">My Test</a>
 * <p>
 * <b>Note</b>Make sure to use the value of <i>target</i> as a 
 * single string, as this tag is following same standard adopted
 * by other built-in tags, where following text will represent the
 * <i>title</i> of the link to the specified <i>target</i>.
 * 
 * @see WikipediaTaglet#toString(Tag)
 * 
 * @author Bruno Braga &lt;bruno.braga@gmail.com&gt;
 * 
 * @since 1.0
 */
public class WikipediaTaglet implements Taglet {
    
    /**
     * Holds the URI address of the Wikipedia website, as <i>{@value URI}</i>.
     */
    private final String URI = "http://en.wikipedia.org/";
    /**
     * Holds the name of the this custom tag, as <i>{@value NAME}</i>.
     */
    private static final String NAME = "wikipedia";
    /**
     * Return the name of this custom tag, as <i>{@value NAME}</i>.
     */
    public String getName() { return NAME; }
    /**
     * The <code>wikipedia</code> tag can be used in field comment documentation.
     */
    public boolean inField() { return true; }
    /**
     * The <code>wikipedia</code> tag can be used in constructor comment documentation.
     */
    public boolean inConstructor() { return true; }
    /**
     * The <code>wikipedia</code> tag can be used in method comment documentation.
     */
    public boolean inMethod() { return true; }
    /**
     * The <code>wikipedia</code> tag can be used in overview comment documentation.
     */
    public boolean inOverview() { return true; }
    /**
     * The <code>wikipedia</code> tag can be used in package comment documentation.
     */
    public boolean inPackage() { return true; }
    /**
     * The <code>wikipedia</code> tag can be used in type comment documentation.
     */
    public boolean inType() { return true; }
    /**
     * The <code>wikipedia</code> tag can be used in inline comment documentation.
     */
    public boolean isInlineTag() { return true; }
    
    /**
     * Method used to register this tag.
     * 
     * @param tagletMap  the map to register this tag to, used internally by javadoc.
     */
    @SuppressWarnings("unchecked")
    public static void register(Map tagletMap) {
       WikipediaTaglet tag = new WikipediaTaglet();
       Taglet t = (Taglet) tagletMap.get(tag.getName());
       if (t != null) {
           tagletMap.remove(tag.getName());
       }
       tagletMap.put(tag.getName(), tag);
    }

    /**
     * Renders the <i>{&#064;wikipedia target[ title]}</i> tag as a HTML
     * code in the format: 
     * <pre>
     * {@code
     *     <a href="http://en.wikipedia.org/{target}">{title||target}</a>
     * }
     * </pre>
     * <b>Note</b>: 
     * <ul>
     *         <li>If no <i>target</i> is informed, <i>title</i> will be used in its place.</li>
     *         <li>Make sure to use the value of <i>target</i> as a single string, as this tag 
     *             is following same standard adopted by other built-in tags, where following 
     *             text will represent the <i>title</i> of the link to the specified <i>target</i>.</li>
     * </ul>
     * 
     * @param tag the tag representation of this custom tag, used internally by javadoc.
     * 
     * @return the string representation of the Wikipedia website link,
     *            following the pattern as documented above.
     *             <p>
     *             <b>Attention</b>: If badly specified (eg. no target), the returning value will 
     *             be an red colored error string, to call attention about the issue to be resolved.
     */
    public String toString(Tag tag) {

        if (tag.text() != null && tag.text().length() > 0) {
            String[] temp = tag.text().split(":");
            if (temp.length > 1 && temp[1].length() > 0) {
                String title = temp[1];
                for(int i = 2; i < temp.length; i++)
                    title += " " + temp[i];
                return "<a href=" + this.URI + temp[0] + ">" + title + "</a>";
            }
            else
                return "<a href=" + this.URI + temp[0] + ">" + temp[0] + "</a>";
        }
        return "<font color=\"#FF0000\">#ERROR! {Wikipedia tag}</font>";
    }
    
    /**
     * This method should not be called since arrays of inline tags do not
     * apply for this tag. The method {@link #toString(Tag)} should be used 
     * instead to convert this inline tag to a string.
     * 
     * @param tags the array of tags representing of this custom tag, used 
     * internally by javadoc.
     */
    public String toString(Tag[] tags) { return null; }
}

