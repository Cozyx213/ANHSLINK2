document.addEventListener("DOMContentLoaded", () => {



    const times = document.querySelectorAll(".time");
    times.forEach((time) => {
        time.innerHTML = `${getTime(time.innerHTML)} ago`;
        console.log(time)
    });





    function getTime(time) {
        let now = new Date();
        let minuteNow = now.getMinutes();
        let HourNow = now.getHours();
        let DayNow = now.getDate();
        let regex = /(\w{3})\. (\d{1,2}), (\d{4}), (\d{1,2}):(\d{2}) (a\.m\.|p\.m\.)/;
        
        const matches = time.match(regex);
        if (matches) {
            const month = matches[1];
            const day = parseInt(matches[2]);
            const year = matches[3];
            let hour = parseInt(matches[4]);
            let minute = parseInt(matches[5]);
            const period = matches[6];
            console.log(day, DayNow)
            //const ago = minuteNow - minute;



            if (period === 'p.m.') {
                hour += hour+ 12;
            }

            let minDiff = minuteNow - minute;
        




            if (day===DayNow && HourNow - hour === 0) {
                let minuteAgo = minuteNow - minute;
                return `${minuteAgo}min`
            } else if (day < DayNow ){
                HourNow += 24;
                let ago = HourNow - hour;
                console.log(hour, HourNow)
                return `${ago}hr`
            }

        }
    }









})