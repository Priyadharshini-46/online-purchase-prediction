exports.handler = async function (event) {
    try {
        const data = JSON.parse(event.body);

        // Temporary test response
        return {
            statusCode: 200,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                prediction: "No Purchase",
                message: "Netlify Function is working!"
            })
        };

    } catch (error) {
        return {
            statusCode: 400,
            body: JSON.stringify({
                error: "Invalid request"
            })
        };
    }
};