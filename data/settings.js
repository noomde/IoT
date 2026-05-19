module.exports = {
    uiPort: process.env.PORT || 1880,
    credentialSecret: process.env.NODE_RED_CREDENTIAL_SECRET,
    flowFile: "flows.json",
    functionExternalModules: true,

    disableEditor: true,
    
    ui: {
        path: "/"
    }
};
