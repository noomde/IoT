module.exports = {
    uiPort: process.env.PORT || 1880,
    credentialSecret: process.env.NODE_RED_CREDENTIAL_SECRET,
    flowFile: "flows.json",
    functionExternalModules: true,

    adminAuth: {
        type: "credentials",
        users: [{
            username: process.env.NODE_RED_ADMIN_USER,
            password: process.env.NODE_RED_ADMIN_PASSWORD_HASH,
            permissions: "*"
        }]
    },
    
    ui: {
        path: "/"
    }
};
