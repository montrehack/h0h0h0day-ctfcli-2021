const express = require('express');
const sqlite3 = require('sqlite3');


const app = express();
const port = 8888;
const db = new sqlite3.Database('./santa.sqlite');

app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.post('/view-list', async (req, res) => {
    const name = req.body.name;
    let list = {};
    let extra = {};

    const anti_injection_pattern = /'/g; // 1 quoty boi vs 1 hacker...
    const isForbidden = (str) => anti_injection_pattern.test(str);

    switch (req.header('X-Mas-Debug')) {
        case 'version':
            extra = await db.query('SELECT sqlite_version()');
            break;
        case 'is-name-on-list':
            const anotherName = req.body.nameOnList;
            if (!isForbidden(anotherName)) {
                extra = await db.query(`SELECT count(*) FROM list WHERE full_name LIKE '%${anotherName}%'`);
            } 
            break;
        default:
            break;
    }

    if (isForbidden(name)) {
        return res.status(400).send({ 'error': 'Hacker detected'});
    }

    list = await db.query(`SELECT * FROM list WHERE attitude='Naughty' AND full_name LIKE '%${name}%'`)
    res.json({ 'data': list, 'debug': extra });
})

// Bad promise wrapper, it's ugly but the vuln is not here
db.query = function (sql, params) {
    var that = this;
    return new Promise(function (resolve, reject) {
        that.all(sql, params, function (error, rows) {
            if (error) {
                resolve({ rows: [], error: error }); // Yeah that's ugly
            }
            else {
                resolve({ rows: rows });
            }
        });
    });
};

app.listen(port, () => {
    console.log(`App started.`)
});