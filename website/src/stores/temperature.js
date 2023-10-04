import { atom, map } from "nanostores";

const active = atom(true);
const temperatures = map({});

const addTemperature = (order, temperature_limit, visible) => {
	temperatures.setKey(order, { temperature_limit, visible });
};

const updateTemperature = (order, temperature_limit, visible) => {
	temperatures.setKey(order, { temperature_limit, visible });
};

export { active, temperatures, addTemperature, updateTemperature };
