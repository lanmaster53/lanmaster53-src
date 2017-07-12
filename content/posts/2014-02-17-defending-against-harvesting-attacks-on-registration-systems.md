title: Defending Against Harvesting Attacks on Registration Systems
publish: True
categories: [application security]

The most obvious challenge to preventing harvesting on registration systems is that the application must ask for a unique piece of information with which to identify the applicant. In most cases, this piece of information is the username. If we enforce this distinction during the traditional registration process and provide visual feedback, then we create the possibility for username harvesting.

<!-- READMORE -->

The typical user account registration system will ask for the applicant to provide all of the information required to create an account on a registration page. When the registration page is submitted, the application validates the uniqueness of the username. The application then responds with one of the following messages:

- An account with matching data already exists.
- The account is created.
- An activation link has been sent to the email address provided in the registration data.

This behavior can be leveraged to harvest valid users of the application by attempting to register accounts with suspected usernames and analyzing the responses. There are several traditional defenses to this type of attack on registration pages:

- CAPTCHAs. CAPTCHAs can be used to slow automated attacks on this behavior. However, an attacker can still leverage this vulnerability over time, attempt to bypass the CAPTCHA system, or script through the CAPTCHA restriction using a third party CAPTCHA answering service.
- Blocking. Blocking at a lower level of the OSI model can also be used to prevent automated attacks on this behavior. However, if the blocking system is not implemented correctly, it can lead to an unintentional Denial-of-Service vulnerability. In addition, blocks that target a source IP address are easily circumvented by spreading requests across open proxies.
- Approval. A system requiring the manual approval of new accounts by a system administrator is another way to mitigate attacks on this behavior. However, this adds the element of human interaction which has administrative ramifications in terms of time required to monitor and manage the system, as well as possible exploitation of the approving authority.

A quick solution to this problem would be to discard custom usernames and enforce the use of an email address as the unique ID for all accounts. Then, respond to registration requests with a generic message stating that "An email regarding the steps remaining to register has been sent to the provided email address." regardless of whether the information provided matches an existing account. If an account matching the email address provided already exists, then a notice is sent. If a matching account does not exist, then a one-time-use account activation link is sent. The account should not be created until activation has occurred.

A variation of the previous solution changes the order of events. Instead of gathering applicant information in the registration form, it would require only an email address. When the email address is submitted to the registration form, the application responds with a similar generic message such as, "An email regarding the steps remaining to register has been sent to the provided email address." regardless of whether the email address provided matches an existing account. If an account matching the email address provided already exists, then a notice is sent. If a matching account does not exist, then a one-time-use registration link is sent to the address for the user to complete the registration process.

The above solutions are very similar, with the main difference being when the email is sent. In the first solution, the email is sent **after** the applicant's information has been given, so the email contains an activation link. In the second solution, the email is sent **before** the applicant's information has been given, so the email contains a registration link. Either solution solves the problem, but depending on the current registration system, one solution may be easier to implement than the other. The bottom line is, there are two keys to making a registration system impervious to harvesting attacks:

- Force the use of an email address as the username, or unique ID, for user accounts.
- Provide a consistent response to registration requests.

Enforcing the use of an email address as the username provides benefits in other areas as well. Developers won't be required to maintain reversible versions of passwords, as reseting a password would be as simple as sending a password reset link to the registered email address. The need for a password could actually be completely removed by implementing a login system where users can authenticate by using a one-time-use link sent to them by submitting their email address to a login form. This places the burden of authentication on the email system, which in most enterprises is managed internally or by a trusted third party. There's also the administrative benefit of an email address being much easier for users to remember across multiple applications than custom usernames.

Just something to consider the next time someone asks for a secure away to handle user registration.
