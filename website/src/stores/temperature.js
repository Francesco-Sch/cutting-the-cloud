import { atom, map } from "nanostores";
import { persistentAtom } from "@nanostores/persistent";

const active = persistentAtom("active", true, {
	encode: JSON.stringify,
	decode: JSON.parse,
});
const temperatures = map({});

const addTemperature = (order, temperature_limit, visible) => {
	temperatures.setKey(order, { temperature_limit, visible });
};

const updateTemperature = (order, temperature_limit, visible) => {
	temperatures.setKey(order, { temperature_limit, visible });
};

export { active, temperatures, addTemperature, updateTemperature };
