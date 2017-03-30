#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

username = ""
email = ""

class MainHandler(webapp2.RequestHandler):
    def get(self):

        header = """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="stylesheet.css" />
            <title>Signup</title>
        </head>
        <body>
        """

        footer = """
        </body>
        </html>
        """

        # TODO 1: Create a form that asks for the following:
        #   1. Name
        #   2. Password
        #   3. Password Verify
        #   4. E-mail (optional)
        # And posts to a validation handler

        form = """
        <form action="/welcome" method="post">
            <table>
                <tr>
                    <th/>
                    <th>Signup</th>
                </tr>
                <tr>
                    <td><label><span class="alert">*</span>Username:</label></td>
                    <td><input type="text" name="username" value="{0}" required /></td>
                </tr>
                <tr>
                    <td><label><span class="alert">*</span>Password:</label></td>
                    <td><input type="password" name="password" required /></td>
                </tr>
                <tr>
                    <td><label><span class="alert">*</span>Confirm Password:</label></td>
                    <td><input type="password" name="confirm-password" required /></td>
                </tr>
                <tr>
                    <td><label>E-Mail:</label></td>
                    <td><input type="email" name="email" value="{1}" /></td>
                </tr>
                <tr>
                    <td colspan="2">
                        <input type="submit" />
                    </td>
                </tr>
            </table>
        </form>
        """.format(username, email)
        body = form

        # TODO 3: Check for and display error
        error = self.request.get("er")
        if error:
            body = """
            {0}
            <p>
                <span class="alert">Passwords do not match.</span>
            </p>
            """.format(body)

        content = header + body + footer
        self.response.write(content)

class SignupHandler(webapp2.RequestHandler):
    def post(self):

        # TODO 2: Validate the user's input
        #   - If valid, redirect to welcome page
        #   - If invalid, redirect back to main page and send an error message
        pwd = self.request.get("password")
        pwd_match = self.request.get("confirm-password")

        global username
        username = cgi.escape(self.request.get("username"))
        global email
        email = cgi.escape(self.request.get("email"))

        if pwd != pwd_match:
            self.redirect("/?er=1")

        self.response.write('Welcome, {0}!'.format(username))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', SignupHandler)
], debug=True)
