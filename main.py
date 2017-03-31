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
import re

username = ""
email = ""

def regex_validate(text, regex):
    validate = re.compile(r"{0}".format(regex))
    return validate.match(text)

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

        values = ["" for i in range(6)]

        values[4] = username
        values[5] = email

        # TODO 3: Check for and display error
        errors = self.request.get("er")
        if errors:
            errors = errors.split(",")
            errors = map(int, errors)

            error_list = [
                "Invalid username",
                "Invalid password",
                "Passwords do not match",
                "Invalid e-mail address"
            ]

            for error in errors:
                values[error] = error_list[error]


        # TODO 1: Create a form that asks for the following:
        #   1. Name
        #   2. Password
        #   3. Password Verify
        #   4. E-mail (optional)
        # And posts to a validation handler

        form = """
        <form action="welcome" method="post">
            <table>
                <tr>
                    <th/>
                    <th>Signup</th>
                </tr>
                <tr>
                    <td><label><span class="alert">*</span>Username:</label></td>
                    <td><input type="text" name="username" value="{4}" required /></td>
                    <td><span class="alert">{0}</span></td>
                </tr>
                <tr>
                    <td><label><span class="alert">*</span>Password:</label></td>
                    <td><input type="password" name="password" required /></td>
                    <td><span class="alert">{1}</span></td>
                </tr>
                <tr>
                    <td><label><span class="alert">*</span>Confirm Password:</label></td>
                    <td><input type="password" name="confirm-password" required /></td>
                    <td><span class="alert">{2}</span></td>
                </tr>
                <tr>
                    <td><label>E-Mail:</label></td>
                    <td><input type="email" name="email" value="{5}" /></td>
                    <td><span class="alert">{3}</span></td>
                </tr>
                <tr>
                    <td/>
                    <td><input type="submit" /></td>
                </tr>
            </table>
        </form>
        """.format(values[0], values[1], values[2], values[3], values[4], values[5])
        body = form

        content = header + body + footer
        self.response.write(content)

class SignupHandler(webapp2.RequestHandler):
    def post(self):

        # TODO 2: Validate the user's input
        #   - If valid, redirect to welcome page
        #   - If invalid, redirect back to main page and send an error message

        errs = []

        # Validate username
        global username
        username = self.request.get("username")
        if not regex_validate(username, "^[a-zA-Z0-9_-]{3,20}$"):
            errs.append("0")
        username = cgi.escape(username)

        # Validate password
        pwd = self.request.get("password")
        if not regex_validate(pwd, "^.{3,20}$"):
            errs.append("1")

        # Verify passwords match
        pwd_match = self.request.get("confirm-password")
        if pwd != pwd_match:
            errs.append("2")

        # Validate e-mail
        global email
        email = self.request.get("email")
        if not regex_validate(email, "^[\S]+@[\S]+\.[\S]+$"):
            errs.append("3")
        email = cgi.escape(email)

        # Redirect if validation failed
        if len(errs) > 0:
            err_string = ",".join(errs)
            self.redirect("/?er={0}".format(err_string))
        else:
            self.response.write('Welcome, {0}!'.format(username))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', SignupHandler)
], debug=True)
